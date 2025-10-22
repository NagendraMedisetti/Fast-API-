from fastapi.testclient import TestClient
from main import app, get_current_user  # import the actual dependency function
 
client = TestClient(app)
 
def fake_user():
   return {"username": "test_user"}


 
def test_me_override():
   app.dependency_overrides[get_current_user] = fake_user
   try:
       resp = client.get("/me?token=secret")
       assert resp.status_code == 200
       assert resp.json() == {"hello": "test_user"}
   finally:
       app.dependency_overrides.pop(get_current_user, None)


 