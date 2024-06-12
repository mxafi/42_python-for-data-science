import sys as s


def isInt(i: str) -> bool:
    try:
        int(i)
        return True
    except ValueError:
        return False


def whatis():
    if len(s.argv) == 1:
        return
    try:
        assert len(s.argv) < 3, "more than one argument is provided"
    except AssertionError as e:
        print(f"{e.__class__.__name__}: {e}")
        return

    try:
        assert isInt(s.argv[1]), "argument is not an integer"
    except AssertionError as e:
        print(f"{e.__class__.__name__}: {e}")
        return

    input = int(s.argv[1])
    if input % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


whatis()
