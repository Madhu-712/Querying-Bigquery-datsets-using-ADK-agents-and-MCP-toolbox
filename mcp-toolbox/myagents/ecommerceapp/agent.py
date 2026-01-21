from google.adk.agents.llm_agent import Agent



from google.adk.agents import Agent
from toolbox_core import ToolboxSyncClient

toolbox = ToolboxSyncClient("http://127.0.0.1:5000")

# Load all the tools
tools = toolbox.load_toolset('my_bq_toolset')

root_agent = Agent(
    name="ecommerce_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about ecommerce."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the ecommerce data. Use the tools to answer the question"
    ),
    tools=tools,
)
