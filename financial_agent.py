from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()

## Web Search Agent
web_search_agent=Agent(
    name="web_search_agent",
    role='Search information from web',
    model=Groq(id='llama3-70b-8192'),
    tools=[DuckDuckGo()],
    instructions=['Always include sources'],
    show_tools_calls=True,
    markdown=True
)


## Financial Agent
financial_agent=Agent(
    name="financial AI Agent",
    role='Search financial information',
    model=Groq(id='llama3-70b-8192'),
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True,company_news=True)],
    instructions=['use table to display the source'],
    show_tools_calls=True,
    markdown=True
)

multi_ai_agent=Agent(
    team=[web_search_agent,financial_agent],
    model=Groq(id='llama3-70b-8192'),
    instructions=['Always include sources',"use table to display the data"],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for nvidia", stream=True, markdown=True)  

