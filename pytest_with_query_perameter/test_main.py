from fastapi.testclient import TestClient
from main import app
 
client = TestClient(app)
 
def test_add_numbers():
   response = client.get("/add?a=5&b=10")
   assert response.status_code == 200
   assert response.json() == {"result": 15}
 
def test_create_user():
   response = client.post("/users", json={"name": "Avinash", "email": "avinash@example.com"})
   assert response.status_code == 200
   data = response.json()
   assert data["status"] == "created"
   assert data["user"]["name"] == "Avinash"