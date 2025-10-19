from fastapi.responses import FileResponse
from fastapi import HTTPException
from fastapi import FastAPI

app=FastAPI()
@app.get("/download/{filename}")
def download_file(filename: str):
   safe_name = Path(filename).name  # Prevent path traversal
   file_path = UPLOAD_DIR / safe_name
 
   if not file_path.exists():
       raise HTTPException(status_code=404, detail="File not found")
 
   # Return file as downloadable response
   return FileResponse(
       path=file_path,
       filename=safe_name,
       media_type="application/octet-stream"
   )