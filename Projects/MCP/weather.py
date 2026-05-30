from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
def get_weather(Location:str)->str:
    "it is mock function to return the rainy weather"
    return f"it always rainy in {Location}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")