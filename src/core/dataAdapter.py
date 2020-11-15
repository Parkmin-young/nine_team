import os
import numpy as np
import PIL.Image as pilimg
import matplotlib.pyplot as plt

PATH = os.path.dirname(__file__)
PATH_IMGS = PATH + "/../../data"

def __loadFromDir(path: str):
    arrays = []
    for fileName in os.listdir(PATH_IMGS + "/" + path):
        if fileName == "readme.md":
            continue
        array = pilimg.open(PATH_IMGS + "/" + path + "/" + fileName)
        array = array.resize((512,512))
        array = np.array(array)

        #  ARRAY 전처리
        arrays.append(array)

    arrays = np.array(arrays)
    arrays = arrays / 255.0

    if(len(arrays) == 0):
        arrays = arrays.reshape((0, 512, 512, 3))

    return arrays


def loadMemory():
    train_knu = __loadFromDir("train/knu")
    train_none_knu = __loadFromDir("train/none-knu")
    test_knu = __loadFromDir("test/knu")
    test_none_knu = __loadFromDir("test/none-knu")

    train_x = np.concatenate([train_knu, train_none_knu])
    train_y = np.concatenate([np.ones(train_knu.shape[0]), np.zeros(train_none_knu.shape[0])])
    test_x = np.concatenate([test_knu, test_none_knu])
    test_y = np.concatenate([np.ones(test_knu.shape[0]), np.zeros(test_none_knu.shape[0])])

    return (train_x, train_y, test_x, test_y)


if __name__ == "__main__":
    tx, ty, x, y = loadMemory()
    print(tx.shape)