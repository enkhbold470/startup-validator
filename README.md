# Startup Idea Validator

A comprehensive startup idea validation tool that uses AI-powered web search and semantic research to analyze startup ideas.

**Powered by [Dedalus Labs](https://dedalus.ai/)** - An AI agent platform that enables seamless integration with MCP servers for advanced research and analysis.

## Features

- **Market Analysis**: Research market size, growth potential, and trends
- **Competitive Landscape**: Identify direct and indirect competitors
- **Validation Metrics**: Analyze similar successful startups and market demand
- **Risk Assessment**: Identify market risks, technical challenges, and barriers to entry
- **Actionable Recommendations**: Get validation scores and next steps

## How It Works

This validator is powered by **Dedalus Labs**, which orchestrates AI agents with MCP (Model Context Protocol) servers for comprehensive startup analysis.

The system uses two MCP servers through Dedalus Labs:

1. **brave-search-mcp** (`windsor/brave-search-mcp`): Real-time web search for current market data, competitors, and trends
2. **exa-mcp** (`joerup/exa-mcp`): Semantic search for deep analysis and research

## Setup

1. Install dependencies:
```bash
uv pip install -r requirements.txt
```

2. Copy the example environment file and configure your API keys:
```bash
cp .env.example .env
```

3. Set up your environment variables in `.env`:
```
DEDALUS_API_KEY=your_dedalus_api_key_here
```

**Note**: Get your Dedalus Labs API key from [https://dedalus.ai/](https://dedalus.ai/). The MCP servers (exa-mcp and brave-search-mcp) are automatically configured through Dedalus Labs.

## Usage

1. Install dependencies:
```bash
uv pip install -r requirements.txt
```

2. Run the Flask application:
```bash
python main.py
```

3. Open your browser and navigate to:
```
http://localhost:5000
```

4. Fill in the form with:
   - Your startup idea (required)
   - Target market (optional)
   - Budget/Funding stage (optional)

5. Click "Validate Idea" and wait for the comprehensive validation report.

## Web Interface

The application provides a clean, modern web interface with:
- Simple form for input
- Loading indicators during validation
- Formatted results display
- Error handling

## Output

The validator provides:
1. Market analysis with size, trends, and customer insights
2. Competitive landscape analysis
3. Validation metrics and success indicators
4. Risk assessment and challenges
5. Recommendations with validation score (1-10) and next steps

## Requirements

- Python 3.8+
- Dedalus Labs API key (get it from [https://dedalus.ai/](https://dedalus.ai/))
- MCP servers are automatically configured through Dedalus Labs

