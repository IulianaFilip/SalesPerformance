from __future__ import annotations
from fastapi import FastAPI
from datetime import date
from enum import Enum
from sqlmodel import Field, Session, SQLModel, create_engine, select
from pydantic import BaseModel
from typing import Union, Literal # , TypeAlias

app = FastAPI()


class Status(str, Enum):
    Open = "Open"
    Made = "Made"
    Reviewed = "Reviewed"
    Closed = "Closed"

class SeeReport(BaseModel):
    name: str
    quarters: str
    metric_calculations: str
    individual_performance: str
    team_performance: str
    customer_behavior: str


      
class AddChange(BaseModel):
    quarters: str
    category: str
    subcategory: str
    change_made: str
    report_made: str
    output: str
    status: Status = Status.Open
    created_at: date = date.today()
   
class SalePerformance(SQLModel, SeeReport, AddChange ): 
    id: int = Field(default=None, primary_key=True)
    
    class Config:
        orm_mode = True
 
saleperformance_db = []
    

@app.get("/salesperformance")
async def get_report():
    return saleperformance_db

@app.post("/salesperformance1", response_model=SalePerformance)
async def create_change(item: AddChange):
    sale_performance = SalePerformance(**item.dict())
    saleperformance_db.append(sale_performance)
    return sale_performance

Quarter = Literal["Q1", "Q2", "Q3", "Q4"]
Category = Literal["Revenue", "Unit sold", "Conversion rate"]
Subcategory = Literal["Sales targets", "Achived sales", "Conversion rate"]
Change_made = Literal["Team targets", "Overall revenue", "Conversion rate"]
Report_made = Literal["Patterns", "Trends", "segment customer"]
Output = Literal["Patterns", "Trends", "segment customer"]
    
@app.post("/salesperformance2")
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
