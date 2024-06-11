import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """
    Calculates the BMI value for a given list of heights and weights,
    outputs a list of BMI values.
    """
    try:
        assert len(height) == len(weight), "input list length mismatch"
        assert all(isinstance(item, (int, float)) for item in height), \
            "height must be a list of ints or floats"
        assert all(isinstance(item, (int, float)) for item in weight), \
            "weight must be a list of ints or floats"
        a = np.array([height, weight])
        assert a[a < 0].size == 0, "values have to be positive and non-zero"

        h = a[0, :]
        assert h[h > 3].size == 0, "heights have to be under 3 meters"
        assert h[h < 1].size == 0, "heights have to be over 1 meter"
        w = a[1, :]
        assert w[w > 300].size == 0, "weights have to be under 300 kilograms"
        assert w[w < 20].size == 0, "weights have to be over 20 kilograms"

        bmi = w / (h**2)
        return list(bmi)
    except AssertionError as e:
        print(f"{e.__class__.__name__}: {e}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Takes a list of numbers and some limiting integer,
    return a list of booleans that represent the items in the list of
    numbers
    """
    pass


def main():
    """Testmain for give_bmi and apply_limit"""
    pass


if __name__ == "__main__":
    main()

bm = give_bmi([1.8, 1.7, 1.6], [80, 70, 60])
print(bm)
