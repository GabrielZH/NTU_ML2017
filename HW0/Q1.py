import sys

import numpy as np
import matplotlib.pyplot as plt


def multiply_matrices(f1, f2):
    try:
        # read matrix A and B from the 2 text files respectively
        mtxA = np.loadtxt('./' + f1)
        mtxB = np.loadtxt('./' + f2)

        # use method matmul() to operate matrix multiplication
        mulmtx = np.matmul(mtxA, mtxB)

        # reshape mutmtx to 1D
        np.reshape(mulmtx, (1, np.size(mulmtx)))

        # sort the matrix and save it into a text file
        sortedmtx = sorted(mulmtx)

    except Exception:
        print("Files do not exist under current path")
        print("Please put this script and target files under the same path")

    f = open('./ans_one.txt', 'wt')

    for element in sortedmtx:
        f.write(str(element) + "\n")

    f.close()

if __name__ == '__main__':
    multiply_matrices(sys.argv[1], sys.argv[2])

