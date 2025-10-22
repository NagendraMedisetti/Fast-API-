from fastapi.testclient import TestClient
from main import app, SessionLocal, User

client = TestClient(app)

def test_create_user():
    payload = {"username": "Avinash", "email": "avinash@example.com"}
    response = client.post("/users", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["username"] == payload["username"]
    assert data["email"] == payload["email"]

    # Optional: Verify data in DB (integration-level check)
    db = SessionLocal()
    user = db.query(User).filter_by(email=payload["email"]).first()
    db.close()

    assert user is not None
    assert user.username == "Avinash"