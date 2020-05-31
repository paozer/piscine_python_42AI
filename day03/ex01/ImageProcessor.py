import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class ImageProcessor:
    @staticmethod
    def load(self, path):
        arr = mpimg.imread(path)
        print(f"{arr.shape[0]} x {arr.shape[1]}")
        return arr

    @staticmethod
    def display(self, array):
        plt.imshow(array)
