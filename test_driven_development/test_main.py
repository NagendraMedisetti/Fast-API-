from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

   
def test_can_vote_if_age_is_more_than_18():
      response = client.get("/vote/20")
      assert response.status_code == 200
      data = response.json()
      assert data["message"] == "You can vote"
   
def test_can_vote_if_age_is_18():
   response = client.get("/vote/18")
   assert response.status_code == 200
   data = response.json()
   assert data["message"] == "You can vote"

def test_cannot_vote_if_age_is_less_than_18():
   response = client.get("/vote/16")
   assert response.status_code == 200
   data = response.json()
   assert data["message"] == "You cannot vote"