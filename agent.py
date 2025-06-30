from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from tools import search_tool
from langchain.agents import create_react_agent, AgentExecutor

# Initialize the local LLM (Llama 3) using Ollama
llm = ChatOllama(model="llama3")

# Define the prompt template for the agent, enforcing tool use and the ReAct format
# The agent is instructed to always use a tool and never answer from its own knowledge
# After providing the 'Final Answer', the agent must stop
# The template also injects the available tools and their names
# The agent_scratchpad variable is used by LangChain to keep track of the reasoning steps

template = """
You are an AI assistant that must always use the available tools to answer questions. Do not answer directly from your own knowledge.

Question: {input}
{agent_scratchpad}

Use the following format:
Thought: Do I need to use a tool? Yes
Action: <tool name>
Action Input: <input to the tool>
Observation: <tool result>
Thought: I have the information needed.
Final Answer: <answer based on tool result>

After you provide 'Final Answer:', stop and do not continue. Never repeat the cycle after the final answer.

TOOLS:
{tools}
Tool names: {tool_names}
"""

prompt = ChatPromptTemplate.from_template(template)

# Register the available tools for the agent
tools = [search_tool]

# Create the ReAct agent with the LLM, tools, and prompt
agent = create_react_agent(llm, tools, prompt)

# Create the AgentExecutor, which manages the agent's reasoning and tool use
# max_iterations limits the number of reasoning steps to avoid infinite loops
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True, max_iterations=1)

def run_agent_query(query: str):
    """
    Runs a query through the LangChain agent and prints the result.
    """
    print(f"\n--- Agentic AI Example (LangChain + Ollama) ---")
    print(f"Query: '{query}'")
    response = agent_executor.invoke({"input": query})
    print(f"Agent Response: {response['output']}\n")

if __name__ == '__main__':
    # Run example queries to demonstrate agentic AI
    run_agent_query("Current weather in madrid")
    run_agent_query("What is the population of paris?")
    run_agent_query("What is the capital of brazilian guiana?")