from __future__ import annotations
from fastapi import FastAPI, Depends, HTTPException
from datetime import date
from enum import Enum
from sqlmodel import Field, Session, SQLModel, create_engine, select
from pydantic import BaseModel
from typing import Optional

from typing import List

sql_file_name = "database.db"
sqlite_url = f"sqlite:///{sql_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


class Status(str, Enum):
    Open = "Open"
    InProgress = "InProgress"
    Closed = "Closed"


class SeeReport(SQLModel):
    name: str
    quarters: str
    metric_calculations: str
    individual_performance: str
    team_performance: str
    customer_behavior: str


class AddChange(SQLModel):
    quarters: str
    category: str
    subcategory: str
    change_made: str
    report_made: str
    output: str
    status: Status = Status.Open
    created_at: date = date.today()


class ChangeCreate(AddChange):
    pass


class ChangeRead(AddChange):
    id: int


    
class SalesPerformance(SQLModel, table=True):
    

    id: Optional[int] = Field(default=None, primary_key=True)
    quarters: str
    category: str
    subcategory: str
    change_made: str
    report_made: str
    output: str


class Config:
    orm_mode = True


app = FastAPI()


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/salesperformance", response_model=List[SalesPerformance])
async def get_report(*, session: Session = Depends(get_session)):
    sales_performance = session.query(SalesPerformance).all()
    return sales_performance
  

@app.post("/salesperformance", response_model=SalesPerformance)
async def sales_performance(sales_data: SalesPerformance, session: Session = Depends(get_session)):
    sales_performance_entry = SalesPerformance(
        quarters=sales_data.quarters,
        category=sales_data.category,
        subcategory=sales_data.subcategory,
        change_made=sales_data.change_made,
        report_made=sales_data.report_made,
        output=sales_data.output
    )
    session.add(sales_performance_entry)
    session.commit()
    return sales_performance_entry

