from multiprocessing import Pool

import click

from . import FILES_DIR, WORKING_DIR, utils
from .convert import Converter


def do_work(file_data):
    converter = Converter(file_data[0], file_data[1])
    converter.convert()


@click.command()
@click.option("-f", "--filetype", default="mp3")
@click.argument("inpath", default=WORKING_DIR)
def main(filetype, inpath):
    file_objs = utils.dir_scan(inpath, True)
    paths = []
    for file_obj in file_objs:
        paths.append([filetype, file_obj.path])

    with Pool(6) as pool:
        pool.map(do_work, paths)


if __name__ == "__main__":
    main()
