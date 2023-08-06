import os
from pathlib import Path

WORKING_DIR = Path.cwd()
PROJECT_ROOT_DIR = os.path.abspath(os.curdir)
FILES_DIR = Path(PROJECT_ROOT_DIR, "files")
