from pathlib import Path
from cx_Freeze import Executable, setup

folder = Path(__file__).resolve().parent
# The freezer bundles the game with the images it loads while drawing the snake.
assets = [(str(folder / name), name) for name in ("apple2.png", "snakehead2.png")]
setup(
    name="Slither",
    version="1.0",
    options={"build_exe": {"packages": ["pygame"], "include_files": assets}},
    executables=[
        Executable(str(folder / "39_PythonGameDevelopment.py"), target_name="Slither")
    ],
)
