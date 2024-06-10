from sys import argv as av


def isValidStr(input_string: str) -> bool:
    """Checks if a string contains any special characters"""
    for c in input_string:
        if not c.isalnum() and not c == " ":
            return False
    return True


def generateMorseDict() -> dict:
    """Generates the dictionary of ascii to morse pairs"""
    return {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. "
    }


def ascii_to_morse(input: str) -> str:
    """Converts ascii string to morse code, outputs string"""
    morse_dict = generateMorseDict()
    output = str()
    for c in input:
        uc = c.upper()
        output += morse_dict[uc]
    return output.rstrip()


def main():
    """
    Program takes a string as an argument and encodes it into Morse Code
    """
    ac = len(av)
    try:
        assert ac == 2, "wrong number of arguments"
        assert isValidStr(av[1]), "string is invalid for morse"
    except AssertionError as e:
        print(f"{e.__class__.__name__}: {e}")
        exit(1)
    print(ascii_to_morse(av[1]))


if __name__ == "__main__":
    main()
