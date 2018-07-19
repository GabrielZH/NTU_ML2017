import sys

import numpy as np
import matplotlib.pyplot as plt


def filter_modification(f1, f2):
    try:
        # load 2 pics via matplotlib.imread
        lena_origin = plt.imread('./' + f1)
        lena_modify = plt.imread('./' + f2)

        # filter the modified part
        diff = lena_modify - lena_origin

        plt.imshow(diff)

    except Exception:
        print("Files do not exist under current directory")
        print("Please put this script and target files under the same directory")

if __name__ == '__main__':
    filter_modification(sys.argv[1], sys.argv[2])
