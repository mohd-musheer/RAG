from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def sum(a:int,b:int)->int:
    "take input 2 numbers and return there sum"
    return a+b

@mcp.tool()
def mull(a:int,b:int)->int:
    "return mulltiplication"
    return a*b

if __name__ == "__main__":
    mcp.run(transport="stdio")