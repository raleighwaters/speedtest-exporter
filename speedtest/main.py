from contextlib import asynccontextmanager

from fastapi import FastAPI, Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

from speedtest.speedtest import start_background_speedtest

@asynccontextmanager
async def lifespan(app: FastAPI):
    start_background_speedtest()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
