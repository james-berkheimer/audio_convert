import os
import subprocess
from pathlib import Path

from .. import FILES_DIR

filename = "down_in_it.flac"
filepath = Path(FILES_DIR, filename)


def flac_to_mp3():
    name, ext = os.path.splitext(filepath)
    file_in = os.path.join(FILES_DIR, filepath)
    file_out = os.path.join(FILES_DIR, f"{name}_converted.mp3")
    print(f"Converting: {file_in}\n" f"To: {file_out}")
    subprocess.call(
        [
            "ffmpeg",
            "-i",
            file_in,
            "-ab",
            "320k",
            "-map_metadata",
            "0",
            file_out,
        ]
    )
