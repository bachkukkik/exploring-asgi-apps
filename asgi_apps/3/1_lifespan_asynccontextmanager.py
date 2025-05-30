from contextlib import asynccontextmanager
from fastapi import FastAPI
from starlette.applications import Starlette
import uvicorn

@asynccontextmanager
async def lifespan(app):
    print("Startup application")
    yield
    print("Shutdown application")

    
app = Starlette(lifespan=lifespan)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)