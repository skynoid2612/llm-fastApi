import os
from langchain import PromptTemplate
from langchain.llms import OpenAI
from config import OPENAI_API_KEY, model_name

try:
    llm = OpenAI(model_name=model_name)
except:
    print("Error while loading the model")
    exit()


def generate_response(prompt: str) -> dict:
    # Your LLM model code here
    try:
        response = llm(prompt)
        return {"prompt_response": response,
                "message": "Success", "status": 1}
    except Exception as ex:
        traceback.print_exc()
        return {"prompt_response": None,
                "message": "Error", "status": 0}
