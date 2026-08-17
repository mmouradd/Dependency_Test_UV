"""
Lightweight persistence layer using TinyDB (a simple JSON document store).
"""

from tinydb import TinyDB, Query

from src.config import DB_PATH

db = TinyDB(DB_PATH)
summaries_table = db.table("post_summaries")


def save_summary(summary_records: list[dict]):
    """Insert (or replace) post-count summary records, keyed by userId."""
    UserQuery = Query()
    for record in summary_records:
        summaries_table.upsert(record, UserQuery.userId == record["userId"])


def get_all_summaries() -> list[dict]:
    return summaries_table.all()
