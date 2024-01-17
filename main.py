from typing import Union

from fastapi import FastAPI

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models import User

engine = create_engine("sqlite:///mydb.db", echo=True)
session = Session(engine)

app = FastAPI()


@app.get("/")
async def read_root():
    user = select(User).where(User.first_name.contains("test"))
    user = session.scalars(user).one()
    return {"Hello": user.first_name}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
