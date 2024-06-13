class calculator:
    """This class can perform some operations on vectors."""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """This method calculates the dot product of two vectors."""
        print("Dot product is: ", sum(x * y for x, y in zip(V1, V2)))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """This method adds two vectors."""
        res = [float(x + y) for x, y in zip(V1, V2)]
        print(f"Add Vector is : {res}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """This method subtracts two vectors."""
        res = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {res}")
