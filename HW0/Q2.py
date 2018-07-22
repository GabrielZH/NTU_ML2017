import sys

import numpy as np
import matplotlib.pyplot as plt


def filter_modification(f1, f2):
    try:
        # load 2 pics via matplotlib.imread
        lena_origin = plt.imread('./' + f1)
        lena_modify = plt.imread('./' + f2)

        # filter the modified part
        img_shape = np.shape(lena_origin)
        diff = np.zeros(shape=img_shape)
        
        for i in img_shape[0]:
            for j in img_shape[1]:
                if lena_origin[i, j] != lena_modified[i, j]:
                    diff[i, j] = lena_modified[i, j]
        

        plt.imshow(diff)

    except Exception:
        print("Files do not exist under current directory")
        print("Please put this script and target files under the same directory")

if __name__ == '__main__':
    filter_modification(sys.argv[1], sys.argv[2])
