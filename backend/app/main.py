from __future__ import annotations
from fastapi import FastAPI,Depends, HTTPException
from datetime import date
from enum import Enum
from sqlmodel import Field, Session, SQLModel, create_engine, select

from typing import Union, Literal # , TypeAlias

sql_file_name = "database.db"
sqlite_url = f"sqlite:///{sql_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)    

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    
def get_session():
    with Session(engine) as session:
        yield session


class Status(str, Enum):
    Open = "Open"
    Made = "Made"
    Reviewed = "Reviewed"
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

    class Config:
        orm_mode = True
        
class ChangeCreate(SeeReport, AddChange):
    pass
class ChangeRead(SeeReport, AddChange):
    id: int
class SalePerformance(SeeReport, AddChange): 
    id: int = Field(default=None, primary_key=True)
    
    
    class Config:
        orm_mode = True
 


app = FastAPI() 

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    

@app.get("/salesperformance", response_model=list[SalePerformance])
async def get_report(*, session: Session = Depends(get_session)):
    salesperformance = session.exec(select(ChangeRead)).all()
    return salesperformance

@app.post("/salesperformance1", response_model=SalePerformance)
async def create_change(*, change: ChangeCreate, session: Session = Depends(get_session)):
    db_change = SalePerformance(**change.dict())
    session.add(db_change)
    session.commit()
    session.refresh(db_change)
    return db_change
    

Quarter = Literal["Q1", "Q2", "Q3", "Q4"]
Category = Literal["Revenue", "Unit sold", "Conversion rate"]
Subcategory = Literal["Sales targets", "Achived sales", "Conversion rate"]
Change_made = Literal["Team targets", "Overall revenue", "Conversion rate"]
Report_made = Literal["Patterns", "Trends", "segment customer"]
Output = Literal["Patterns", "Trends", "segment customer"]
    
@app.post("/salesperformance2", response_model=SalePerformance)
async def create_change(quarters: Quarter, category: Category, subcategory: Subcategory, change_made: Change_made, report_made:Report_made, output:Output):
    change = {
        "quarters": quarters,
        "category": category,
        "subcategory": subcategory,
        "change_made": change_made,
        "report_made": report_made,
        "output": output
    }
    return change

