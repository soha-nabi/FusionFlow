# No-Code Workflow Builder Application

A comprehensive visual workflow builder that enables users to create intelligent AI-powered workflows using drag-and-drop components.
Fusion Flow
link: https://meek-puppy-c79e35.netlify.app/

## 🚀 Features

- **Visual Workflow Builder**: Drag-and-drop interface using React Flow
- **Four Core Components**:
  - User Query: Entry point for user input
  - Knowledge Base: Document upload and processing
  - LLM Engine: AI language model integration
  - Output: Chat interface for responses
- **Real-time Configuration**: Dynamic component configuration panels
- **Interactive Chat**: Built-in chat interface for workflow execution
- **API Integration**: Support for OpenAI, Gemini, SerpAPI, and Brave Search
- **Document Processing**: Upload and process PDF, TXT, and DOCX files

## 🛠️ Tech Stack

- **Frontend**: React 18 + TypeScript + Vite
- **UI Framework**: Tailwind CSS
- **Workflow Engine**: React Flow
- **Icons**: Lucide React
- **State Management**: React Hooks

## 📋 Prerequisites

Before running the application, you'll need API keys for:

- **OpenAI API** (Required): [Get API Key](https://platform.openai.com/api-keys)
- **Google Gemini API** (Required): [Get API Key](https://makersuite.google.com/app/apikey)
- **SerpAPI** (Optional): [Get API Key](https://serpapi.com/)
- **Brave Search API** (Optional): [Get API Key](https://api.search.brave.com/)

## 🚀 Quick Start

### 1. Clone and Install

```bash
# Clone the repository
git clone <repository-url>
cd workflow-builder

# Install dependencies
npm install
```

### 2. Configure Environment Variables

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your API keys
VITE_OPENAI_API_KEY=your_openai_api_key_here
VITE_GEMINI_API_KEY=your_gemini_api_key_here
VITE_SERP_API_KEY=your_serpapi_key_here
VITE_BRAVE_API_KEY=your_brave_search_api_key_here
```

### 3. Start Development Server

```bash
npm run dev
```

The application will be available at `http://localhost:5173`

## 🎯 How to Use

### Building a Workflow

1. **Drag Components**: From the left panel, drag components onto the canvas
2. **Connect Components**: Click and drag between component handles to create connections
3. **Configure Components**: Click on any component to configure its settings in the right panel
4. **Validate Workflow**: Ensure you have at least one User Query, LLM Engine, and Output component

### Required Workflow Structure

- **Start**: User Query component (entry point)
- **Process**: LLM Engine component (AI processing)
- **End**: Output component (display results)
- **Optional**: Knowledge Base component (document context)

### Component Configuration

#### User Query Component
- **Placeholder Text**: Customize the input placeholder

#### Knowledge Base Component
- **Enable/Disable**: Toggle knowledge base functionality
- **Max Documents**: Set maximum number of documents to process
- **Chunk Size**: Configure text chunking size for embeddings
- **Upload Documents**: Add PDF, TXT, or DOCX files

#### LLM Engine Component
- **Model Selection**: Choose between GPT-4, GPT-3.5, Gemini Pro, or Claude 3
- **Temperature**: Control response creativity (0-1)
- **Max Tokens**: Set maximum response length
- **Web Search**: Enable/disable web search integration
- **Custom Prompt**: Add custom instructions for the AI

#### Output Component
- **Format**: Choose between Chat, JSON, or Text output
- **Display Mode**: Select Streaming or Complete response

### Executing Workflows

1. **Build Stack**: Click "Build Stack" to validate and prepare your workflow
2. **Chat with Stack**: Click "Chat with Stack" to open the interactive chat interface
3. **Ask Questions**: Type your questions and receive AI-powered responses

## 🔧 API Configuration

The application uses a centralized API configuration system located in `src/config/api.ts`. This file manages:

- API endpoints and base URLs
- Authentication headers
- Model configurations
- Service integrations

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `VITE_OPENAI_API_KEY` | OpenAI API key for GPT models | Yes |
| `VITE_GEMINI_API_KEY` | Google Gemini API key | Yes |
| `VITE_SERP_API_KEY` | SerpAPI key for web search | No |
| `VITE_BRAVE_API_KEY` | Brave Search API key | No |

## 🏗️ Architecture

### Frontend Structure

```
src/
├── components/           # React components
│   ├── nodes/           # Workflow node components
│   ├── ComponentLibrary.tsx
│   ├── ConfigurationPanel.tsx
│   ├── ChatInterface.tsx
│   └── WorkflowControls.tsx
├── config/              # Configuration files
│   └── api.ts          # API configuration
├── services/            # API service classes
│   └── apiService.ts   # Service implementations
├── types/               # TypeScript type definitions
│   └── workflow.ts     # Workflow-related types
└── App.tsx             # Main application component
```

### Component Architecture

- **Modular Design**: Each component is self-contained with its own configuration
- **Type Safety**: Full TypeScript support with comprehensive type definitions
- **Service Layer**: Abstracted API calls through service classes
- **Configuration Management**: Centralized API and environment configuration

## 🔮 Future Enhancements

### Backend Integration (FastAPI)
- Document processing with PyMuPDF
- Vector storage with ChromaDB
- Embedding generation and similarity search
- Workflow persistence and execution logs

### Database Integration (PostgreSQL)
- User authentication and authorization
- Workflow saving and loading
- Chat history persistence
- Document metadata storage

### Advanced Features
- Real-time collaboration
- Workflow templates
- Advanced analytics and monitoring
- Custom component creation

## 🐛 Troubleshooting

### Common Issues

1. **API Key Errors**: Ensure all required API keys are properly set in the `.env` file
2. **CORS Issues**: API calls may be blocked by CORS policies in development
3. **Component Connection**: Ensure components are properly connected before execution

### Development Tips

- Use the browser's developer tools to monitor API calls
- Check the console for detailed error messages
- Validate your workflow structure before execution

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Support

For support and questions, please open an issue in the GitHub repository.
