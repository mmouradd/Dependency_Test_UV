"""
FastAPI app exposing the pipeline as an HTTP endpoint.
Run with: uv run uvicorn api.app:app --reload
"""

from fastapi import FastAPI

from src.fetcher import fetch_data
from src.processor import process_data
from src.store import save_summary, get_all_summaries
from utils.logger import logger

app = FastAPI(title="uv-python-project API")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/report")
async def report():
    logger.info("handling_report_request")
    raw = await fetch_data()
    processed = process_data(raw)

    summary = processed["summary"]
    records = summary.to_dicts() if summary is not None else []
    save_summary(records)
    return records


@app.get("/summaries")
async def summaries():
    return get_all_summaries()
