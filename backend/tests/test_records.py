from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_create_business_record():

    payload = {
        "record_name": "Test Revenue Report",
        "department": "Finance",
        "amount": 50000,
        "status": "PENDING",
        "description": "Test business record"
    }

    response = client.post(
        "/api/v1/records/",
        json=payload
    )

    assert response.status_code == 201
    assert response.json()["record_name"] == "Test Revenue Report"


def test_invalid_record():

    payload = {
        "record_name": "",
        "department": "Finance",
        "amount": -100
    }

    response = client.post(
        "/api/v1/records/",
        json=payload
    )

    assert response.status_code == 422