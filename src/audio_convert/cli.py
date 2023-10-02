from multiprocessing import Pool

import click

from . import WORKING_DIR, utils
from .convert import Converter


def do_work(file_data):
    converter = Converter(file_data[0], file_data[1])
    converter.convert()


@click.command()
@click.option("-f", "--filetype", default="mp3")
@click.argument("inpath", default=WORKING_DIR, type=click.Path(resolve_path=True))
def main(filetype, inpath):
    paths = []
    for dir_obj in utils.dir_scan(inpath):
        for file_obj in utils.dir_scan(dir_obj, True):
            if file_obj.suffix not in [".jpg", ".png"]:
                paths.append([filetype, file_obj])

    with Pool(6) as pool:
        pool.map(do_work, paths)


if __name__ == "__main__":
    main()
