from fastapi import FastAPI, BackgroundTasks
from datetime import datetime, timedelta, timezone
app = FastAPI()
IST = timezone(timedelta(hours=5, minutes=30))
def get_ist_timestamp() -> str:
   now = datetime.now(IST)
   return now.strftime("%Y-%m-%d %H:%M:%S")

def write_audit_log(message: str):
        timestamp = get_ist_timestamp()
        with open("audit.log", "a") as f:
            f.write(f"[{timestamp}] {message}\n")


@app.post("/order")
def place_order(customer_email: str, background_tasks: BackgroundTasks):
   background_tasks.add_task(write_audit_log, f"Order placed for {customer_email}")
   return {
       "status": "order received",
       "timestamp": get_ist_timestamp()
   }