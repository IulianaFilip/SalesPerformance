from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


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


    