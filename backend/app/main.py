from __future__ import annotations
from fastapi import FastAPI, Depends, HTTPException

from datetime import date
from enum import Enum

from sqlmodel import Field, Session, SQLModel, create_engine, select

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
    category: str
    subcategory: str
    
    
class SalesPerformance(SeeReport, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    

    
class ChangeCreate(SeeReport):
    pass


class AddChange(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    report_id: int = Field(foreign_key="salesperformance.id")
    change_made: str
    report_made: str
    output: str
    status: Status = Status.Open
    created_at: date = date.today()
 
    


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
    sales_performance = session.exec(select(SalesPerformance)).all()
    return sales_performance
 
 
@app.get("/salesperformance/{report_id}/changes", response_model=List[AddChange])
async def get_changes_for_report(report_id: int, session: Session = Depends(get_session)):
    changes = session.exec(select(AddChange).where(AddChange.report_id == report_id)).all()
    return changes
 

@app.post("/salesperformance", response_model=SalesPerformance)
async def create_report(*, sales_performance: ChangeCreate, session: Session = Depends(get_session)):
    db_sales = SalesPerformance.from_orm(sales_performance)
    session.add(db_sales)
    session.commit()
    session.refresh(db_sales)
    return db_sales

@app.post("/salesperformance/{report_id}/change", response_model=AddChange)
async def create_change(report_id: int, change: AddChange, session: Session = Depends(get_session)):
    db_change = AddChange.from_orm(change)
    db_change.report_id = report_id
    session.add(db_change)
    session.commit()
    session.refresh(db_change)
    return db_change
