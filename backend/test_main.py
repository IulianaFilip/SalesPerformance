from app.main import app, SalesPerformance
from fastapi.testclient import TestClient
import pytest

client = TestClient(app)



@pytest.fixture
def valid_payload():
    return {
        "quarters": "Q1",
        "category": "Revenue",
        "subcategory": "Sales Target",
        "change_made": "Team Targets",
        "report_made": "Sales Targets",
        "output": "Sales Targets",
    }

def test_sales_performance_route(valid_payload):
    headers = {
        "Content-Type": "application/json"
    }
    response = client.post("/salesperformance", json=valid_payload, headers=headers)
    
    assert response.status_code == 200
    assert "id" in response.json() 

def test_sales_performance_get():
    response = client.get("/salesperformance")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)  
   



   

    
        
      






