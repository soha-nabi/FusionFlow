import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Dict, Any
import openai
import chromadb
from dotenv import load_dotenv

# --- Setup & Initialization ---

load_dotenv() # Load environment variables from .env file

# Initialize OpenAI Client
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    print("Warning: OPENAI_API_KEY not found. Please set it in backend/.env")

# Initialize ChromaDB Client (in-memory for simplicity)
chroma_client = chromadb.Client()

# Create a sample collection (in a real app, this would be more persistent)
try:
    collection = chroma_client.get_collection(name="documents")
except ValueError:
    collection = chroma_client.create_collection(name="documents")
    # Add some sample documents
    collection.add(
        documents=[
            "The first rule of Fight Club is: you do not talk about Fight Club.",
            "The second rule of Fight Club is: you DO NOT talk about Fight Club!",
            "The sky above the port was the color of television, tuned to a dead channel.",
            "It was a bright cold day in April, and the clocks were striking thirteen."
        ],
        ids=["doc1", "doc2", "doc3", "doc4"]
    )

app = FastAPI()

# --- Pydantic Models ---

class WorkflowNode(BaseModel):
    id: str
    type: str
    data: Dict[str, Any]

class WorkflowEdge(BaseModel):
    id: str
    source: str
    target: str

class Workflow(BaseModel):
    nodes: List[WorkflowNode]
    edges: List[WorkflowEdge]

class RunWorkflowRequest(BaseModel):
    workflow: Workflow
    query: str

# --- API Endpoint ---

@app.post("/run-workflow")
async def run_workflow(request: RunWorkflowRequest):
    nodes_map = {node.id: node for node in request.workflow.nodes}
    edges_map = {edge.source: edge.target for edge in request.workflow.edges}
    
    start_node = next((n for n in request.workflow.nodes if n.type == 'customInput'), None)
    if not start_node:
        raise HTTPException(status_code=400, detail="Workflow must have a User Query component.")

    context = ""
    current_node_id = start_node.id
    path = [start_node.data.get('label', 'User Query')]
    llm_node = None

    # Traverse workflow to find knowledge base and LLM
    while current_node_id in edges_map:
        next_node_id = edges_map[current_node_id]
        current_node = nodes_map.get(next_node_id)
        if not current_node: break

        path.append(current_node.data.get('label', 'Unknown Step'))

        # If it's a knowledge base, query ChromaDB
        if current_node.type == 'knowledgeBase':
            try:
                results = collection.query(query_texts=[request.query], n_results=2)
                context = "\n\nContext from Knowledge Base:\n- " + "\n- ".join(results['documents'][0])
            except Exception as e:
                print(f"Error querying ChromaDB: {e}")
                context = "\n\n(Could not retrieve context from Knowledge Base.)"

        # If it's an LLM, we stop here to process it
        if current_node.type == 'llm':
            llm_node = current_node
            break
        
        current_node_id = next_node_id

    if not llm_node:
        raise HTTPException(status_code=400, detail="No LLM component found in the workflow.")

    # Call OpenAI API
    if not openai.api_key:
        return {"response": "OpenAI API key is not configured. Please set it in `backend/.env`."}

    try:
        prompt = f"Based on the following context, please answer the user's query.\n{context}\n\nUser Query: {request.query}"
        
        chat_completion = openai.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant answering questions based on a user's workflow.",
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            model="gpt-3.5-turbo",
        )
        response_text = chat_completion.choices[0].message.content
    except Exception as e:
        print(f"Error calling OpenAI: {e}")
        raise HTTPException(status_code=500, detail=f"An error occurred with the OpenAI API: {e}")

    return {"response": response_text}

@app.get("/")
async def root():
    return {"message": "FlowFusion Backend is running."}
