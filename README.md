# uv-python-project

A small multi-folder Python project managed with **uv** (`pyproject.toml` + `uv.lock`).
Same shape as a pip/requirements project, but with a different, more diverse set of
dependencies: async HTTP, a web framework, a fast dataframe library, a document DB,
schema validation, structured logging, a CLI framework, and job scheduling.

## Structure

```
uv-python-project/
├── pyproject.toml           # deps managed by uv
├── uv.lock                    # resolved lockfile
├── config.yaml                 # runtime config (yaml instead of .env)
├── src/
│   ├── __init__.py
│   ├── config.py                # loads config.yaml (pyyaml)
│   ├── fetcher.py                # async HTTP fetch (httpx)
│   ├── processor.py               # data transform (polars)
│   └── store.py                    # lightweight JSON document store (tinydb)
├── api/
│   ├── __init__.py
│   └── app.py                      # HTTP API exposing the pipeline (fastapi + uvicorn)
├── utils/
│   ├── __init__.py
│   ├── logger.py                    # structured logging (structlog)
│   ├── schemas.py                    # data validation models (marshmallow)
│   └── scheduler.py                   # recurring background jobs (apscheduler)
├── scripts/
│   └── cli.py                          # standalone CLI (typer)
└── tests/
    ├── __init__.py
    └── test_processor.py                # unit tests (pytest)
```

## Dependencies (`pyproject.toml`)
httpx, fastapi, uvicorn, polars, pyyaml, typer, tinydb, marshmallow, structlog, apscheduler
(+ pytest as a dev dependency)

## Usage

```bash
uv sync

# Run the pipeline once
uv run python -m scripts.cli run

# Run the pipeline on a recurring schedule
uv run python -m scripts.cli watch

# Run the FastAPI server
uv run uvicorn api.app:app --reload   # then visit http://localhost:8000/report

# Run tests
uv run pytest
```
