from sys import argv as av
from ft_filter import ft_filter as f


def isInt(i: str) -> bool:
    """Checks if the input string is convertable to an integer"""
    try:
        int(i)
        return True
    except ValueError:
        return False


def isValidStr(input_string: str) -> bool:
    """Checks if a string contains any special characters"""
    for c in input_string:
        if not c.isalnum() and not c.isspace():
            return False
    return True


def filterstring(S: str, N: int) -> list:
    """
    Takes string S and integer N, outputs a list of words
    from S that have a length greater than N
    Assumes that words are seperated only by spaces,
    S contains only space and alnum characters,
    N is positive.
    """
    SS = S.split()
    SSF = f(lambda s: len(s) > N, SS)
    filtered_list = []
    for item in SSF:
        filtered_list.append(item)
    return filtered_list


def main():
    """
    Takes a string S and an integer N,
    outputs a list of words seperated by spaces,
    where the words have a length greater that N.
    """
    ac = len(av)
    try:
        assert ac == 3, "wrong number of arguments"
        assert isValidStr(av[1]), "first argument not a valid string"
        assert isInt(av[2]), "second argument not an integer"
        assert int(av[2]) >= 0, "integer value must be positive"
    except AssertionError as e:
        print(f"{e.__class__.__name__}: {e}")
        exit(1)
    FS = filterstring(av[1], int(av[2]))
    print(FS)


if __name__ == "__main__":
    main()
