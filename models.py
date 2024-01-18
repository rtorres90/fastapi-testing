from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    email: Mapped[email] = mapped_column(String(50))
    expenses: Mapped[List["Expense"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    incomes: Mapped[List["Income"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    budget: Mapped["Budget"] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r})"
    
class Budget(Base):
    __tablename__ = "budget"
    id: Mapped[int] = mapped_column(primary_key=True)
    budget_name: Mapped[str] = mapped_column(String(30))
    amount: Mapped[int]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="budget")

class Expense(Base):
    __tablename__ = "expense"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    amount: Mapped[int]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="expenses")
    type_of_expense_id: Mapped[int] = mapped_column(ForeignKey("type_of_expense.id"))
    type_of_expense: Mapped["TypeOfExpense"] = relationship("TypeOfExpense")
    def __repr__(self) -> str:
        return f"Expense(id={self.id!r}, title={self.title!r}), amount={self.amount!r})"

class TypeOfExpense(Base):
    __tablename__ = "type_of_expense"
    id: Mapped[int] = mapped_column(primary_key=True)
    type_name: Mapped[str]
    def __repr__(self) -> str:
        return f"Income(id={self.id!r}, title={self.title!r}), amount={self.amount!r})"

class Income(Base):
    __tablename__ = "income"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    amount: Mapped[int]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="incomes")
    typo_of_income_id: Mapped[int] = mapped_column(ForeignKey("type_of_income.id"))
    type_of_income: Mapped["TypeOfIncome"] = relationship("TypeOfIncome")
    def __repr__(self) -> str:
        return f"Income(id={self.id!r}, title={self.title!r}), amount={self.amount!r})"

class TypeOfIncome(Base):
    __tablename__ = "type_of_income"
    id: Mapped[int] = mapped_column(primary_key=True)
    type_name: Mapped[str]
    def __repr__(self) -> str:
        return f"Income(id={self.id!r}, title={self.title!r}), amount={self.amount!r})"

