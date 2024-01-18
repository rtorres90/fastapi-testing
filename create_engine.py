from sqlalchemy import create_engine
from models import Base, User, TypeOfExpense, TypeOfIncome, Budget, Expense, Income

engine = create_engine("sqlite:///mydb.db", echo=True)

Base.metadata.create_all(engine)

from sqlalchemy.orm import Session


with Session(engine) as session:
    test_user = User(
        first_name="test",
        last_name="test",
        email="test@mailinator.com"
    )

    test_user2 = User(
        first_name="test2",
        last_name="test2",
        email="test@mailinator.com"
    )
    session.add_all([test_user, test_user2])
    session.commit()

    type_of_income1 = TypeOfIncome(type_name="Sueldo")
    type_of_income2 = TypeOfIncome(type_name="Devolución")
    type_of_income3 = TypeOfIncome(type_name="Otros")


    session.add_all([type_of_income1, type_of_income2, type_of_income3])
    session.commit()

    type_of_expenses1 = TypeOfExpense(type_name="Comida")
    type_of_expenses2=TypeOfExpense(type_name="Transporte")
    type_of_expenses3=TypeOfExpense(type_name="Ropa")
    type_of_expenses4=TypeOfExpense(type_name="Cuentas")
    type_of_expenses5=TypeOfExpense(type_name="Otros")

    session.add_all([type_of_expenses1, type_of_expenses2, type_of_expenses3, type_of_expenses4, type_of_expenses5])
    session.commit()

    bugdet = Budget(budget_name="Presupuesto mensual", amount=400000, user=test_user)
    session.add(bugdet)
    session.commit()

    income = Income(name="Sueldo", amount=400000, type_of_income=type_of_income1, user=test_user)

    expenses1 = Expense(name="compra 1", amount=1000, user=test_user, type_of_expense=type_of_expenses1)
    expenses2 = Expense(name="compra 2", amount=10000, user=test_user, type_of_expense=type_of_expenses4)

    session.add_all([expenses1, expenses2])
    session.commit()