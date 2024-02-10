from typing import Final
from pathlib import Path

BASE_DIR: Final[Path] = Path(__file__).resolve().parent.parent.parent
SIMULATION_DATA_PATH: Final[str] = f'{BASE_DIR}/data'
ENVIRONMENT_COLLECTION_PATH: Final[str] = f'{BASE_DIR}/environments'
SOURCE_PATH: Final[str] = f'{BASE_DIR}/src'
TESTS_PATH: Final[str] = f'{BASE_DIR}/tests'
UI_PATH: Final[str] = f'{BASE_DIR}/ui'
UI_ASSETS_PATH: Final[str] = f'{UI_PATH}/assets'
