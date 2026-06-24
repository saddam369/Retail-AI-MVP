from langchain_ollama import ChatOllama
import requests
from app.config import MODEL_NAME
from app.config import OLLAMA_URL

def generate_answer(question,result):

    prompt = f"""
Question:
{question}

Database Result:
{result}

Generate a short business answer.
"""

    llm=ChatOllama(model="llama3.2:latest")
    response = llm.invoke(prompt)
    res = response.content
    print(res)
    return res