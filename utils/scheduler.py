"""
Background job scheduling using APScheduler.
Runs the pipeline on a recurring interval instead of once.
"""

import asyncio

from apscheduler.schedulers.background import BackgroundScheduler

from src.config import SCHEDULER_INTERVAL_MINUTES
from utils.logger import logger


def start_scheduler(job_fn):
    """Schedule job_fn (an async callable) to run on a fixed interval."""
    scheduler = BackgroundScheduler()

    def run_job():
        logger.info("scheduled_job_triggered")
        asyncio.run(job_fn())

    scheduler.add_job(run_job, "interval", minutes=SCHEDULER_INTERVAL_MINUTES)
    scheduler.start()
    logger.info("scheduler_started", interval_minutes=SCHEDULER_INTERVAL_MINUTES)
    return scheduler
