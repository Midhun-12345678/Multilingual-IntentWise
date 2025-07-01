from fastapi import FastAPI
from app.router import router

app = FastAPI(
    title="IntentWise: Multilingual Intent API",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def read_root():
    return {"status": "🚀 IntentWise API is running"}