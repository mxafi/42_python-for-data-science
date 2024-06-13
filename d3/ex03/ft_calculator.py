class calculator:
    """A class to perform basic operations on a list of numbers."""
    def __init__(self, vec) -> None:
        """Initialize the class with a list of numbers."""
        self.vec = vec

    def __add__(self, object) -> None:
        """Add a number to each element of the list."""
        res = [x + object for x in self.vec]
        print(res)
        self.vec = res

    def __mul__(self, object) -> None:
        """Multiply each element of the list by a number."""
        res = [x * object for x in self.vec]
        print(res)
        self.vec = res

    def __sub__(self, object) -> None:
        """Subtract a number from each element of the list."""
        res = [x - object for x in self.vec]
        print(res)
        self.vec = res

    def __truediv__(self, object) -> None:
        """Divide each element of the list by a number."""
        if object == 0:
            print("Error: Division by zero is not possible")
            return
        res = [x / object for x in self.vec]
        print(res)
        self.vec = res
