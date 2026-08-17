"""
Processes raw data into a summarized polars DataFrame.
"""

import polars as pl


def process_data(raw_data: list[dict]) -> dict:
    """Convert raw list of dicts into a polars DataFrame with a title-length column."""
    df = pl.DataFrame(raw_data)

    if "title" in df.columns:
        df = df.with_columns(pl.col("title").str.len_chars().alias("title_length"))

    summary = None
    if "userId" in df.columns:
        summary = (
            df.group_by("userId")
            .agg(pl.len().alias("post_count"))
            .sort("userId")
        )

    return {"data": df, "summary": summary}
