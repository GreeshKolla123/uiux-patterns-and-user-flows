from fastapi import FastAPI
from app.routes import main_router
from app.database import engine
from app.config import settings

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await engine.dispose()

app.include_router(main_router)