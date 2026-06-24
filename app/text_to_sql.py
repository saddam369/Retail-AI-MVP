import requests

from app.config import OLLAMA_URL
from app.config import MODEL_NAME
from langchain_openrouter import ChatOpenRouter
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

llm = ChatOpenRouter(
    model="openai/gpt-4o-mini"
)

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

Generate only the SQL query.
Do not use markdown.
Do not wrap the query in ```sql or ``` blocks.
Return plain SQL text only.
"""

def generate_sql(question:str):

    prompt = f"""
    {SCHEMA}

    Question:
    {question}
    """

    response=llm.invoke(prompt)
    res=response.content
    print(res.replace("\n", " ").replace("```sql", ""))
    return res.replace("\n", " ").replace("```sql", "")