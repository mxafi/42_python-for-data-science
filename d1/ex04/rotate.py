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

    # crop/zoom
    height, width = a.shape[:2]
    top = int(0.12 * a.shape[0])
    left = int(0.44 * a.shape[1])
    a = a[top:min(top+400, height), left:min(left+400, width)]

    # convert to greyscale
    a = np.round(np.dot(a[..., :3], [0.2989, 0.5870, 0.1140])).astype(int)

    # reshape for subject expected output
    a_reshaped = a.reshape(a.shape[0], a.shape[1], 1)
    print("The shape of image is:", a_reshaped.shape)
    print(a_reshaped)

    # transpose using list comprehension
    trans = np.array([[a_reshaped[j][i] for j in range(len(a_reshaped))]
                     for i in range(len(a_reshaped[0]))])

    # reshape again for subject expected output
    trans_reshaped = trans.reshape(trans.shape[0], trans.shape[1])

    print("New shape after Transpose:", trans_reshaped.shape)
    print(trans_reshaped)
    plt.imshow(trans_reshaped, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
