"""
Puzzle 11:

Use the os.listdir function to return all files with a given extension
in a directory (and all of its sub-directories).
"""

import os


def list_files(target, ext):

    ext_fnames = []
    for fname in os.listdir(target):
        if fname.endswith(ext):
            ext_fnames.append(fname)
        elif "." not in fname:
            ext_fnames.extend(list_files(f"{target}/{fname}", ext))

    return ext_fnames


if __name__ == "__main__":

    print(list_files("data/p11", ".txt"))
