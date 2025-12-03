# client to test fastmcp client and transports

import asyncio
from fastmcp import Client

client = Client("http://localhost:8000/mcp")


async def call_tool(name: str):
    async with client:
        # Basic server interaction
        await client.ping()

        # List available operations
        tools = await client.list_tools()
        print(tools)
        resources = await client.list_resources()
        print(resources)
        prompts = await client.list_prompts()
        print(prompts)

        # Execute operation
        result = await client.call_tool("greet", {"name": name})
        print(result.content[0].text)


asyncio.run(call_tool("Vishal"))
