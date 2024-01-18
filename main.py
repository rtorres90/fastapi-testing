from typing import Union

from fastapi import FastAPI

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models import Expense

engine = create_engine("sqlite:///mydb.db", echo=True)
session = Session(engine)

app = FastAPI()


@app.get("/expenses/{user_id}")
async def read_item(user_id: int):
    stmt = select(Expense).where(Expense.user_id == user_id)
    expenses = [expense for expense in session.scalars(stmt)]
    return {"expenses": expenses}
