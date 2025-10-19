from fastapi.testclient import TestClient
from main import app
client = TestClient(app)
 
def test_read_root():
   response = client.get("/")
   assert response.status_code == 200
   assert response.json() == {"message": "Hello, FastAPI!"}
 
def test_greet_user():
   response = client.get("/greet/avinash")
   assert response.status_code == 200
   data = response.json()
   assert data["message"] == "Hello, avinash!"