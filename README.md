# Distinguishing Generative AI from Agentic AI

This repository contains example code for the article: [Distinguishing Generative AI from Agentic AI](https://woliveiras.github.io/posts/distinguishing-generative-ai-from-agentic-ai/).

## Overview

The project demonstrates the conceptual and practical differences between GenAI and Agentic AI, using the following examples:

- **Generative AI**: A simple use case that generates a slogan based on a given topic using the Ollama model.
- **Agentic AI**: An AI agent that can perform tasks like web search, using LangChain with Ollama as the LLM. The agent can reason about tasks and use tools.

## Requirements

- Python 3.8+
- [Ollama](https://ollama.com/) installed and running
- The following Ollama models pulled:
  - `llama3`

## Setup

1. **Clone this repository**

```sh
git clone git@github.com:woliveiras/genai-agentic-ai.git
cd genai-agentic-ai
```

2. **Pull the required models with Ollama**

```sh
ollama pull llama3
```

3. **Create and activate a virtual environment**

```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

4. **Install dependencies**

```sh
pip install -r requirements.txt
```

## Running the Examples

```sh
# Run the GenAI example
python genai.py

# Run the Agent example
python agent.py
```

## Files

- `genai.py`: Demonstrates a simple Generative AI use case using Ollama.
- `agent.py`: Shows how to create an AI agent using LangChain with Ollama as the LLM.
- `tools.py`: Contains custom tools for the agent, such as a web search tool.

## References

- [Original Article](https://woliveiras.github.io/posts/distinguishing-generative-ai-from-agentic-ai/)
