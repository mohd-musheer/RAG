from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
from langgraph.prebuilt import create_react_agent
from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv

load_dotenv()

async def main():
    client = MultiServerMCPClient(
        {
            "Math": {
                "command": "python",
                "args": ["Projects/MCP/maths_server.py"], 
                "transport": "stdio"
            },
            "weather": {
                "url":"http://127.0.0.1:8000/mcp",
                "transport": "streamable_http" 
            }
        }
    )
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    
    tools = await client.get_tools()
    model = init_chat_model(
        "groq:openai/gpt-oss-120b"
    )
    agent = create_react_agent(model, tools)
    
    math_response = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "calculate 6 plus 9 into 8 and also what is weather in Nandgaon Peth currently"
                }
            ]
        }
    )
    
    print("response : ", math_response["messages"][-1].content)
    
asyncio.run(main())