"""
Fetches data from a public API using httpx (async).
"""

import httpx

from src.config import REQUEST_TIMEOUT


async def fetch_data() -> list[dict]:
    """Fetch a list of sample posts from a public JSON API."""
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        print(f"Fetch failed, using fallback data. ({e})")
        return [
            {"userId": 1, "id": 1, "title": "sample title", "body": "sample body"},
            {"userId": 2, "id": 2, "title": "another title", "body": "another body"},
        ]
