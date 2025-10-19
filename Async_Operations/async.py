from fastapi import FastAPI, BackgroundTasks
from datetime import datetime, timedelta, timezone
import asyncio
app = FastAPI()
IST = timezone(timedelta(hours=5, minutes=30))
 
def get_ist_timestamp() -> str:
   now = datetime.now(IST)
   return now.strftime("%Y-%m-%d %H:%M:%S")

async def send_email_async(to: str, subject: str):
   await asyncio.sleep(10)  # Simulate delay
   timestamp = get_ist_timestamp()
   with open("email.log", "a") as f:
       f.write(f"[{timestamp}] Sent email to {to}: {subject}\n")
       
@app.post("/order")
def place_order(customer_email: str, background_tasks: BackgroundTasks):
   background_tasks.add_task(send_email_async, customer_email, "Thanks for your order!")
   return {
       "status": "order received",
       "timestamp": get_ist_timestamp()
   }
