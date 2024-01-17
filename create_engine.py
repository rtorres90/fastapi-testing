from sqlalchemy import create_engine
from models import Base, User

engine = create_engine("sqlite:///mydb.db", echo=True)

Base.metadata.create_all(engine)

from sqlalchemy.orm import Session


with Session(engine) as session:
    test_user = User(
        first_name="test",
        last_name="test",
        email="test@mailinator.com"
    )
    session.add_all([test_user])
    session.commit()