from fastapi import FastAPI

from src.summary.router import router as summary_router

app = FastAPI()

app.include_router(summary_router)


@app.get("/")
async def root():
    return {"Coxit": "Hello from Yaroslav Biziuk!!!"}
