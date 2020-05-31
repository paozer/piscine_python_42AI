import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class ImageProcessor:
    def __init__(self):
        pass

    def load(self, path):
        arr = mpimg.imread(path)
        print(f"{arr.shape[0]} x {arr.shape[1]}")
        return arr

    def display(self, array):
        plt.imshow(array)

if __name__ == "__main__":
    imp = ImageProcessor()
    arr = imp.load("rarepepe.png")
    imp.display(arr)
