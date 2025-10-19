from fastapi import FastAPI, File, UploadFile
from datetime import datetime, timedelta, timezone
from pathlib import Path
import shutil
app = FastAPI()
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)
IST = timezone(timedelta(hours=5, minutes=30))


 
def get_ist_timestamp():
   now = datetime.now(IST)
   return now.strftime("%Y-%m-%d %H:%M:%S")


@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
   timestamp = get_ist_timestamp()
   file_name = f"{timestamp.replace(' ', '_').replace(':', '-')}_{file.filename}"
   file_path = UPLOAD_DIR / file_name
 
   with open(file_path, "wb") as buffer:
       shutil.copyfileobj(file.file, buffer)
 
   return {
       "message": "File uploaded successfully!",
       "file_name": file_name,
       "timestamp_ist": timestamp
   }