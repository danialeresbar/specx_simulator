from typing import Final
from pathlib import Path

BASE_DIR: Final[Path] = Path(__file__).resolve().parent.parent.parent
SIMULATION_DATA_PATH: Final[str] = f'{BASE_DIR}/data'
ENVIRONMENT_COLLECTION_PATH: Final[str] = f'{BASE_DIR}/environments'
SOURCE_PATH: Final[str] = f'{BASE_DIR}/src'
UI_PATH: Final[str] = f'{BASE_DIR}/ui'
