import requests

from app.config import OLLAMA_URL
from app.config import MODEL_NAME
from langchain_ollama import ChatOllama

SCHEMA = """
Tables:

products(
id,
product_name,
category,
cost_price,
selling_price
)

branches(
id,
branch_name,
city
)

inventory(
id,
product_id,
branch_id,
stock_qty,
reorder_level
)

sales(
id,
product_id,
branch_id,
quantity,
sale_date,
total_amount
)

shrinkage(
id,
product_id,
branch_id,
quantity_lost,
loss_date
)

Generate ONLY PostgreSQL SQL.
Give me plain text SQL query only.
"""

def generate_sql(question:str):

    prompt = f"""
    {SCHEMA}

    Question:
    {question}
    """
    print(prompt)
    llm = ChatOllama(
        model="llama3.2:latest"
    )

    response=llm.invoke(prompt)
    res=response.content
    return res