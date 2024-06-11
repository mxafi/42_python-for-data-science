from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def main():
    """Program loads an image "animal.jpeg",
    prints info:
    - Size in pixels on X and Y axis
    - Number of channels
    - Pixel content of the image
    "zooms" the image,
    displays the image after zooming
    """
    a = ft_load("animal.jpeg")
    if a.size == 1 and a[0] == "error_load_image":
        return
    print(a)

    im = Image.fromarray(a)
    width, height = im.size
    left = int(0.44 * width)
    top = int(0.12 * height)
    right = min(int(left + 400), width)
    bottom = min(int(top + 400), height)
    im = im.crop((left, top, right, bottom))
    im = ImageOps.grayscale(im)
    a2 = np.array(im)
    a2 = a2.reshape(a2.shape[0], a2.shape[1], 1)
    print("New shape after slicing:", a2.shape)
    print(a2)
    plt.imshow(im, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
