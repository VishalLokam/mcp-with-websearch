# PydanticAI client. PydanticAI supports FastMCPToolset
from pydantic_ai import Agent
from pydantic_ai.toolsets.fastmcp import FastMCPToolset
from dotenv import load_dotenv
import logfire

load_dotenv()
logfire.configure()
logfire.instrument_pydantic_ai()

# connecting to MCP server running as streamable-http on localhost
toolset = FastMCPToolset("http://localhost:8000/mcp", max_retries=5)

agent = Agent(
    "openai:gpt-5-mini",
    toolsets=[toolset],
    system_prompt="You are a helpful assistant. Use `websearch` tool if the user starts the question with search the web or similar wording. ",
)

result = agent.run_sync("search the web for latest news about India")

print(f"Output: {result.output}")
