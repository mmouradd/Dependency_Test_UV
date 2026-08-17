"""
Tests for the processor module.
"""

from src.processor import process_data


def test_process_data_adds_title_length():
    raw = [{"userId": 1, "id": 1, "title": "hello", "body": "world"}]
    result = process_data(raw)
    df = result["data"]
    assert "title_length" in df.columns
    assert df["title_length"][0] == len("hello")


def test_process_data_summary_counts_posts_per_user():
    raw = [
        {"userId": 1, "id": 1, "title": "a", "body": "x"},
        {"userId": 1, "id": 2, "title": "b", "body": "y"},
        {"userId": 2, "id": 3, "title": "c", "body": "z"},
    ]
    result = process_data(raw)
    summary = result["summary"]
    counts = dict(zip(summary["userId"].to_list(), summary["post_count"].to_list()))
    assert counts == {1: 2, 2: 1}
