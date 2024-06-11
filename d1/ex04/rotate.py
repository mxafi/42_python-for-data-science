from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def main():
    """Program loads an image "animal.jpeg",
    cuts a square part of the image,
    transposes and displays the square.
    It also prints the new shape and data of the image
    after the transpose.
    """
    a = ft_load("animal.jpeg")
    if a.size == 1 and a[0] == "error_load_image":
        return

    height, width = a.shape[:2]
    top = int(0.12 * a.shape[0])
    left = int(0.44 * a.shape[1])
    a = a[top:min(top+400, height), left:min(left+400, width)]
    im = Image.fromarray(a)
    im = ImageOps.grayscale(im)
    a = np.array(im)
    a2 = a.reshape(a.shape[0], a.shape[1], 1)
    print("The shape of image is:", a2.shape)
    print(a2)

    transposed = np.array([[a2[j][i] for j in range(len(a2))]
                          for i in range(len(a2[0]))])

    print("New shape after Transpose:", transposed.shape)
    print(transposed)
    plt.imshow(transposed, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
