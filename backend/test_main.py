from app.main import app, SalesPerformance
from fastapi.testclient import TestClient
import pytest
from sqlmodel import Session, engine
client = TestClient(app)

@pytest.fixture
def test_db_session():
    with Session(engine) as session:
        yield session

def test_sales_performance_route():
    payload = {
        "quarters": "Q1",
        "category": "Revenue",
        "subcategory": "Sales Target",
        "change_made": "Team Targets",
        "report_made": "Sales Targets",
        "output": "Sales Targets",
    }
    headers = {
    "Content-Type": "application/json"
}
    response = client.post("/salesperformance", json=payload, headers=headers)
    assert response.status_code == 200

def test_sales_performance_get():
    response = client.get("/salesperformance")
    assert response.status_code == 200
    
    



   

    
        
      






