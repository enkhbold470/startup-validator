import asyncio
from flask import Flask, render_template, request, jsonify
from dedalus_labs import AsyncDedalus, DedalusRunner
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

async def validate_startup_idea(idea: str, target_market: str = "", budget: str = ""):
    """
    Validate a startup idea using web search and semantic research.
    
    Args:
        idea: The startup idea to validate
        target_market: Target market/customer segment (optional)
        budget: Budget or funding stage (optional)
    """
    client = AsyncDedalus()
    runner = DedalusRunner(client)

    validation_prompt = f"""I have a startup idea and need comprehensive validation. Please research and analyze:

STARTUP IDEA: {idea}
{f'TARGET MARKET: {target_market}' if target_market else ''}
{f'BUDGET/FUNDING: {budget}' if budget else ''}

Please use the available search tools (brave-search-mcp and exa-mcp) to research and provide:

1. MARKET ANALYSIS:
   - Market size and growth potential
   - Current market trends
   - Target customer demographics and pain points

2. COMPETITIVE LANDSCAPE:
   - Direct competitors and their offerings
   - Indirect competitors
   - Competitive advantages/disadvantages
   - Market gaps and opportunities

3. VALIDATION METRICS:
   - Similar successful startups/products
   - Market demand indicators
   - Customer acquisition channels
   - Revenue potential and business models

4. RISKS & CHALLENGES:
   - Market risks
   - Technical challenges
   - Regulatory considerations
   - Barriers to entry

5. RECOMMENDATIONS:
   - Validation score (1-10)
   - Key next steps for validation
   - Suggested pivots or improvements
   - Go/no-go recommendation with reasoning

Please be thorough and use multiple search queries to gather comprehensive information."""

    result = await runner.run(
        input=validation_prompt,
        model="openai/gpt-4.1",
        mcp_servers=[
            "joerup/exa-mcp",           # For semantic research and deep analysis
            "windsor/brave-search-mcp"  # For real-time web search and market data
        ]
    )

    return result.final_output

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    """Handle validation request."""
    try:
        data = request.get_json()
        idea = data.get('idea', '').strip()
        target_market = data.get('target_market', '').strip()
        budget = data.get('budget', '').strip()
        
        if not idea:
            return jsonify({'error': 'Startup idea is required'}), 400
        
        # Run async validation
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            validation_result = loop.run_until_complete(
                validate_startup_idea(
                    idea=idea,
                    target_market=target_market,
                    budget=budget
                )
            )
            return jsonify({'result': validation_result})
        finally:
            loop.close()
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
