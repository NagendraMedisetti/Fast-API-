from fastapi import APIRouter, FastAPI

app = FastAPI()
router = APIRouter(prefix="/users", tags=["Users"])
customer=APIRouter(prefix="/customer",tags=["Customer"])

@customer.get("/")
def list_customers():
    return {
        "message": "List of customers",
        "customers": ["Avinash", "Rahul", "Rohan"]
    }
    
@customer.post("/{name}")
def create_customer(name: str):
    return {"message": f"Customer named with {name} created"}   
app.include_router(customer)

@router.get("/")
def list_users():
    return {
        "message": "List of users",
        "users": ["Avinash", "Rahul", "Rohan"]
    }

@router.post("/{name}")
def create_user(name: str):
    return {"message": f"User named with {name} created"}

app.include_router(router)