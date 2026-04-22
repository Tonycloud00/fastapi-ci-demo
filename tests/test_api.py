from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_item():
    response = client.post("/add/apple")
    assert response.status_code == 200
    assert "apple" in response.json()["todos"]

def test_get_todos():
    response = client.get("/todos")
    assert response.status_code == 200