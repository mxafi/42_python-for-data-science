import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes a 2D array, start and ending row index (exclusive)
    Prints the input shape, slices the indexes, prints the output shape
    Returns truncated version of the array based on provided start, end
    """
    try:
        assert type(family) is list, "family must be a list"
        assert type(start) is int, "start must be an int"
        assert type(end) is int, "end must be an int"
        assert all(isinstance(item, list) for item in family), \
            "input list must consist of lists"
        assert len(set(len(sub) for sub in family)) == 1, \
            "all sublists of the input list must have the same length"
        a = np.array(family)
        print("My shape is :", a.shape)
        sa = a[start:end]
        print("My new shape is :", sa.shape)
        return sa.tolist()
    except AssertionError as e:
        print(f"{e.__class__.__name__}: {e}")
        return []


def main():
    """Testmain for slice_me"""
    darray = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("2D Array:", darray)
    start = 1
    print("   start:", start)
    end = 2
    print("     end:", end)
    s = slice_me(darray, start, end)
    print("  sliced:", s)


if __name__ == "__main__":
    main()
