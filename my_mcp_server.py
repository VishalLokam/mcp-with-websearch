from fastmcp import FastMCP

mcp = FastMCP("My MCP server")


@mcp.tool
def greet(name: str) -> str:
    """Greets the user and asks a friendly question"""
    return f"Hello {name}! how can I help you?"


@mcp.tool
def add(a: int, b: int) -> int:
    """Adds two integer numbers together."""
    return a + b


if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="localhost", port=8000)
