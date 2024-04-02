from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

# uvicorn users:app --reload

@app.get("/users")
async def users():
    return "Hola usuarios"


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)
