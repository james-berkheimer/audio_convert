import os
import subprocess
from pathlib import Path


class Converter(object):
    def __init__(self, type_out, file_path_in):
        self._type_out = f".{type_out}"
        self._file_path_in = Path(file_path_in)
        self._file_path_out = self._make_out_path()

    def convert(self):
        try:
            subprocess.call(
                [
                    "ffmpeg",
                    "-i",
                    self._file_path_in,
                    "-ab",
                    "320k",
                    "-map_metadata",
                    "0",
                    self._file_path_out,
                ]
            )
        except Exception as e:
            print(e)

    def _make_out_path(self):
        raw_filename = self._file_path_in.stem
        dirpath = self._file_path_in.parent
        new_dirpath = dirpath.joinpath("_converted")
        new_dirpath.mkdir(exist_ok=True)
        return new_dirpath.joinpath(raw_filename).with_suffix(self._type_out)
