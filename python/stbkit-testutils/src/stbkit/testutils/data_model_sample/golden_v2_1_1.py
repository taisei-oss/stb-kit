from pathlib import Path

from stbkit.core.data_model.stb_v2_1_1 import VERSION, StBridge
from stbkit.core.stb_io import load

CASES_DIR = Path(__file__).parents[6] / "tests" / "fixtures" / "cases"


def golden_v2_1_1_has_extension() -> StBridge:
    PATH = CASES_DIR / "has_extension" / "has_extension.stb_v2_1_1.stb"
    stb: StBridge = load(PATH, version=VERSION)
    return stb
