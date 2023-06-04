from pathlib import Path

BASE_URL="http://localhost:8000"
BASE_URL_REMOTE="https://lopcodeingame.herokuapp.com"
IS_LOCAL=True
APP_PATH: Path = Path("~/lopcodeingame").expanduser()
CONFIG_PATH: Path =  APP_PATH / "config.json"

def get_base_url() -> str:
    return BASE_URL if IS_LOCAL else BASE_URL_REMOTE