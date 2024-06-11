from PIL import Image, UnidentifiedImageError
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image in JPEG (or JPG) format,
    prints its format and its pixels' content in RGB format
    """
    try:
        im = Image.open(path)
        assert im.format == "JPEG", "Image must be in JPEG format"
        assert im.mode == "RGB", "Image must be in RGB mode"
        im_arr = np.array(im)
        return im_arr
    except (AssertionError,
            UnidentifiedImageError,
            FileNotFoundError,
            IsADirectoryError,
            PermissionError
            ) as e:
        print(f"{e.__class__.__name__}: {e}")
        return np.array(["error_load_image"])


def main():
    """Testmain for ft_load"""
    print(ft_load("10by10.jpg"))


if __name__ == "__main__":
    main()
