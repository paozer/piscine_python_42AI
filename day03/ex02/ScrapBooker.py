import numpy as np


class ScrapBooker:
    @staticmethod
    def crop(array, dim, pos=(0, 0)):
        if dim[0] > array.shape[0] or dim[1] > array .shape[1]\
           or dim[0] < 0 or dim[1] < 0:
            print("Error: dim out of bounds")
            return
        return array[pos[0]:pos[0] + dim[0],pos[1]:pos[1] + dim[1]]

    @staticmethod
    def thin(array, n, axis):
        pass

    @staticmethod
    def juxtapose(array, n, axis):
        pass

    @staticmethod
    def mosaic(array, dim):
        pass


if __name__ == "__main__":
    a = np.arange(25).reshape(5,5)
    print("full array\n", a)
    print("\ndim = (2, 3), pos = (0, 0)\n", ScrapBooker.crop(a, (2,3)))
    print("\ndim = (0, 0), pos = (0, 0)\n", ScrapBooker.crop(a, (0,0)))
    print("\ndim = (3, 4), pos = (1, 1)\n", ScrapBooker.crop(a, (3, 4), (1, 1)))
    print("\ndim = (3, 4), pos = (0, 1)\n", ScrapBooker.crop(a, (3, 4), (0, 1)))
    print("\ndim = (3, 4), pos = (1, 0)\n", ScrapBooker.crop(a, (3, 4), (1, 0)))
    print("\ndim = (1, 4), pos = (3, 0)\n", ScrapBooker.crop(a, (1, 4), (3, 0)))
    print("\ndim = (1, 3), pos = (4, 2)\n", ScrapBooker.crop(a, (1, 3), (4, 2)))
    print("\ndim = (13, 0)")
    print(ScrapBooker.crop(a, (13,0)))
