from ImageProcessor import ImageProcessor


if __name__ == "__main__":
    arr = ImageProcessor().load("image.png")
    ImageProcessor().display(arr)
