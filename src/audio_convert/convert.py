import subprocess
from pathlib import Path


class Converter(object):
    def __init__(self, file_ext_out, file_path_in):
        self._file_ext_out = f".{file_ext_out}"
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
        # except Exception as e:
        except subprocess.CalledProcessError as e:
            print(e.output)

    def _make_out_path(self):
        raw_filename = self._file_path_in.stem
        raw_filename = (
            raw_filename.replace("  ", "_")
            .replace(" ", "_")
            .replace(".", "")
            .replace(",", "")
            .replace("'", "")
            .lower()
        )
        dirpath = self._file_path_in.parent
        new_dirpath = dirpath.parent.joinpath("_converted", dirpath.stem)
        new_dirpath.mkdir(parents=True, exist_ok=True)
        return new_dirpath.joinpath(raw_filename).with_suffix(self._file_ext_out)
