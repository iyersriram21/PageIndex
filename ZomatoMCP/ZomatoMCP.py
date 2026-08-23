
from langchain.agents import create_agent
import asyncio
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from dotenv import load_dotenv
load_dotenv()  # Reads OPENAI_API_KEY from .env file


server_params = StdioServerParameters(
    command="npx",
    args=["mcp-remote", "https://mcp-server.zomato.com/mcp"]
)

async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            tools = await load_mcp_tools(session)
            llm = ChatOpenAI(model="gpt-4o")
            agent = create_agent(llm, tools)
            
            # 1. Maintain conversation state in a list
            messages = []
            
            print("🤖 Assistant Ready! Type 'exit' or 'quit' to end.\n")
            
            while True:
                user_input = input("You: ")
                if user_input.lower() in ["exit", "quit"]:
                    break
                
                # Append user prompt
                messages.append(("user", user_input))
                
                # Run agent with full message history
                response = await agent.ainvoke({"messages": messages})
                
                # Update messages history with full agent trajectory (includes tool calls & model replies)
                messages = response["messages"]
                
                # Print the assistant's latest response
                assistant_response = messages[-1].content
                print(f"\nAssistant: {assistant_response}\n")

if __name__ == "__main__":
    asyncio.run(main())