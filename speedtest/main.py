from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI, Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

from speedtest.runner import start_background_speedtest
from speedtest.settings import settings

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    settings.log_settings()
    start_background_speedtest()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
