from fastapi import FastAPI, Request
import time
from datetime import datetime, timedelta, timezone
app = FastAPI()
IST = timezone(timedelta(hours=5, minutes=30))
 
@app.middleware("http")
async def log_requests(request: Request, call_next):
   start_time = time.time()
   start_ts = datetime.now(IST).strftime("%Y-%m-%d %H:%M:%S")

   print(f"[{start_ts}] Incoming request: {request.method} {request.url.path}")
 
   response = await call_next(request)
 
   duration = time.time() - start_time
   print(f"Completed in {duration:.2f}s\n")
 
   return response
 
@app.get("/")
def home():
   return {"message": "Welcome to FastAPI Middleware Demo!"}
 
@app.get("/hello")
def hello():
   return {"greeting": "Hello from /hello route"}
 
 