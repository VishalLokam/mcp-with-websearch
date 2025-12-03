# PydanticAI client. PydanticAI supports FastMCPToolset
from pydantic_ai import Agent
from pydantic_ai.toolsets.fastmcp import FastMCPToolset
from dotenv import load_dotenv

load_dotenv()

# connecting to MCP server running as streamable-http on localhost
toolset = FastMCPToolset("http://localhost:8000/mcp")

agent = Agent("openai:gpt-5", toolsets=[toolset])
