import sys as s


def main():
    """
    Counts and segregates the characters in a string.

    Args:
        One shell argument: the string to count

    Returns:
        None
    """
    argc = len(s.argv)
    try:
        assert argc <= 2, "too many arguments"
    except AssertionError as e:
        print(f"{e.__class__.__name__}: {e}")
        exit(1)
    if argc == 1 or (argc == 2 and s.argv[1] == ""):
        try:
            print("What is the text to count?")
            input_string = s.stdin.readline()
        except EOFError:
            input_string = ""
    else:
        input_string = s.argv[1]
    input_len = len(input_string)
    if input_string[-1] != "\n":
        print("")
    print(f"The text contains {input_len} characters:")
    count_upper = sum(1 for c in input_string if c.isupper())
    count_lower = sum(1 for c in input_string if c.islower())
    punct = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    count_punct = sum(1 for c in input_string if c in punct)
    count_space = sum(1 for c in input_string if c.isspace())
    count_digit = sum(1 for c in input_string if c.isdigit())
    print(f"{count_upper} upper letters")
    print(f"{count_lower} lower letters")
    print(f"{count_punct} punctuation marks")
    print(f"{count_space} spaces")
    print(f"{count_digit} digits")


if __name__ == "__main__":
    main()
