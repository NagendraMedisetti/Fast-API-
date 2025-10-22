from fastapi import FastAPI
 
app = FastAPI()
 
@app.get("/search/{search_term}")
def searchProducts(search_term: str, brand: str = "all_brands"):
    if brand == "all_brands":
        return {"message": f"Searching for {search_term}"}
    else:
        return {"message": f"Searching for {search_term}, and brand is {brand}"}
 
@app.get("/users")
def list_users(active: bool = True, limit: int = 10):
   return {
       "message": "Listing users",
       "active_only": active,
       "limit": limit
   }
 
 