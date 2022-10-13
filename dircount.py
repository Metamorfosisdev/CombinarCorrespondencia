from itertools import count
import pathlib

def countfiles(path):
    count = 0
    for path in pathlib.Path(path).iterdir():
        if path.is_file():
            count += 1

    return count

