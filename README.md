# FastAPI LLM Prompt-Response Generation App

![FastAPI](https://img.shields.io/badge/FastAPI-0.70.0-blue?style=flat-square&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python)

A FastAPI application for generating responses using the LLM (Large Language Model) based on user prompts. This application leverages the power of
FastAPI and the advanced capabilities of LLM to provide contextually relevant responses to user queries.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- FastAPI and Uvicorn (automatically installed from `requirements.txt`)

### Installation

1. Clone the repository to your local machine.

```bash
git clone https://github.com/skynoid2612/llm-fastApi.git
cd fastapi-llm-app
python -m venv venv
source venv/bin/activate  # On Windows, use "venv\Scripts\activate"
pip install -r requirements.txt
export OPENAI_API_KEY=YOUR_API_KEY
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

NOTE: OPENAI_API_KEY can be set from .env file

In this README file, we provide a brief introduction to the FastAPI LLM Prompt-Response Generation App, including information on prerequisites,
installation, running the app, and API endpoints. The API endpoints section demonstrates how to interact with the app's `generate-response` endpoint
with example requests and responses.

Remember to replace `YOUR_API_KEY` with your actual OpenAI API key and update any other specific details relevant to your application in the README.md
file.
