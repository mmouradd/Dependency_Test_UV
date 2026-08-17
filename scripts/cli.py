"""
Typer-based CLI for running the pipeline manually or on a schedule.
Run with: uv run python -m scripts.cli run
         uv run python -m scripts.cli watch
"""

import asyncio

import typer

from src.fetcher import fetch_data
from src.processor import process_data
from src.store import save_summary
from utils.logger import logger
from utils.scheduler import start_scheduler

app = typer.Typer()


async def run_pipeline():
    logger.info("pipeline_started")
    raw = await fetch_data()
    processed = process_data(raw)

    print(processed["data"])

    if processed["summary"] is not None:
        records = processed["summary"].to_dicts()
        save_summary(records)
        logger.info("summary_saved", count=len(records))

    logger.info("pipeline_finished")


@app.command()
def run():
    """Run the pipeline once."""
    asyncio.run(run_pipeline())


@app.command()
def watch():
    """Run the pipeline on a recurring schedule (Ctrl+C to stop)."""
    scheduler = start_scheduler(run_pipeline)
    try:
        typer.echo("Watching... press Ctrl+C to stop.")
        while True:
            pass
    except KeyboardInterrupt:
        scheduler.shutdown()


if __name__ == "__main__":
    app()
