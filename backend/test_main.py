import pytest
from fastapi.testclient import TestClient

from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from app.main import app, get_session

client = TestClient(app)


sqlite_url = "sqlite:///:memory:"


def test_sales_performance_route():
    payload = {
        "quarters": "Q1",
        "category": "Revenue",
        "subcategory": "Sales Target",
        "change_made": "Team Targets",
        "report_made": "Sales Targets",
        "output": "Sales Targets",
        "name" : "Julie",
        "metric_calculations": "Sales Targets",
        "individual_performance": "Sales Targets",
        "team_performance": "Sales Targets",
        "customer_behavior": "Sales Targets",
        
    }
    headers = {
    "Content-Type": "application/json"
}
    response = client.post("/salesperformance", json=payload, headers=headers)
    print(response.json())

    assert response.status_code == 200


def test_get_sales_performance():
    response = client.get("/salesperformance")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

    
        
def test_sales_performance_route_invalid_data():
    payload = {
        # Missing "quarters", "category", and other fields
        "change_made": "Team Targets",
        "report_made": "Sales Targets",
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = client.post("/salesperformance", json=payload, headers=headers)
    assert response.status_code == 422  # 422 Unprocessable Entity







