from langchain_openrouter import ChatOpenRouter
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
llm = ChatOpenRouter(
    model="openai/gpt-4o-mini"
)

def generate_answer(question,result):

    prompt = f"""
Question:
{question}

Database Result:
{result}

Generate a short business answer.
"""

    response = llm.invoke(prompt)
    res = response.content
    print(res)
    return res