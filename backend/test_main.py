from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_sales_performance_route():
    response = client.post("/salesperformance")
    assert response.status_code == 200
    # assert response.json() == {"Hello": "World"}
