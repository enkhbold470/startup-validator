# Startup Idea Validator

A comprehensive startup idea validation tool that uses AI-powered web search and semantic research to analyze startup ideas.

## Features

- **Market Analysis**: Research market size, growth potential, and trends
- **Competitive Landscape**: Identify direct and indirect competitors
- **Validation Metrics**: Analyze similar successful startups and market demand
- **Risk Assessment**: Identify market risks, technical challenges, and barriers to entry
- **Actionable Recommendations**: Get validation scores and next steps

## How It Works

This validator uses two MCP (Model Context Protocol) servers:

1. **brave-search-mcp** (`windsor/brave-search-mcp`): Real-time web search for current market data, competitors, and trends
2. **exa-mcp** (`joerup/exa-mcp`): Semantic search for deep analysis and research

## Setup

1. Install dependencies:
```bash
uv pip install -r requirements.txt
```

2. Set up your environment variables in `.env`:
```
OPENAI_API_KEY=your_openai_api_key_here
```

3. Ensure your MCP servers are configured:
   - `joerup/exa-mcp` should be configured with your Exa API key
   - `windsor/brave-search-mcp` should be configured with your Brave Search API key

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
- OpenAI API key
- Exa API key (for exa-mcp)
- Brave Search API key (for brave-search-mcp)
- Configured MCP servers

