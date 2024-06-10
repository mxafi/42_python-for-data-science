import sys as s

def whatis():
    if len(s.argv) == 1:
        return
    if len(s.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return

    try:
        input = int(s.argv[1])
    except:
        print("AssertionError: argument is not an integer")
        return

    if input % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

whatis()