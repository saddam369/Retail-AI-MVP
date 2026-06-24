from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy import text

from app.database import SessionLocal, Base, engine
from app.schemas import QuestionRequest
from app.text_to_sql import generate_sql
from app.answer_generator import generate_answer
import app.models


@asynccontextmanager
async def lifespan(app: FastAPI):

    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/ask")
def ask(req:QuestionRequest):

    question = req.question

    sql = generate_sql(question)
    print(f"Sql==={sql}")

    forbidden = [
        "DROP",
        "DELETE",
        "UPDATE",
        "ALTER",
        "TRUNCATE",
        "INSERT"
    ]

    upper_sql = sql.upper()

    for word in forbidden:
        if word in upper_sql:
            return {
                "error":"Unsafe SQL detected"
            }
    # rows=["Bread"]
    # answer = generate_answer(
    #         question,
    #         rows
    #     )

    # return {
    #         "question":question,
    #         "sql":sql,
    #         "row":rows,
    #         "answer":answer
    # }        

    db = SessionLocal()

    try:

        result = db.execute(text(sql))

        rows = [dict(row._mapping) for row in result]

        answer = generate_answer(
            question,
            rows
        )

        return {
            "question":question,
            "sql":sql,
            "data":rows,
            "answer":answer
        }

    except Exception as e:

        return {
            "error":str(e)
        }

    finally:
        db.close()