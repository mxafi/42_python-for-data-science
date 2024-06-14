def square(x: int | float) -> int | float:
    """Return the square of x."""
    if isinstance(x, int | float):
        return x * x
    else:
        raise ValueError("x must be an int or a float.")


def pow(x: int | float) -> int | float:
    """Return x to the power of x."""
    if isinstance(x, int | float):
        return x ** x
    else:
        raise ValueError("x must be an int or a float.")


def outer(x: int | float, function) -> object:
    """Return a function that applies the given function to x
    the number of times it's called.
    """
    count = 0

    def inner() -> float:
        """Return the result of applying the function to x, count times."""

        nonlocal count
        res = function(x)
        for _ in range(count):
            res = function(res)
        count += 1
        return res
    return inner
