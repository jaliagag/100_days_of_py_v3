from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI() # instancia de fatapi
favicon_path = "favicon.ico"

@app.get("/")
async def root():
    return "Hola mancito"

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)

@app.get("/health")
async def health():
    return {"ping": "pong"}

@app.get("/url")
async def url():
    return {"url_curso": "https://www.google.com"}

