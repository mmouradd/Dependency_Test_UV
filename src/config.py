"""
Loads runtime configuration from config.yaml.
"""

from pathlib import Path
import yaml

CONFIG_PATH = Path(__file__).resolve().parent.parent / "config.yaml"


def load_config() -> dict:
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)


config = load_config()
REQUEST_TIMEOUT = config["runtime"]["request_timeout"]
DEBUG = config["runtime"]["debug"]
DB_PATH = config["storage"]["db_path"]
SCHEDULER_INTERVAL_MINUTES = config["scheduler"]["interval_minutes"]
