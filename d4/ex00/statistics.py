def check_numbers(numbers: list) -> bool:
    if not numbers:
        return False
    for number in numbers:
        if not isinstance(number, (int, float)):
            return False
    return True


def ft_statistics(*args, **kwargs) -> None:
    numbers = list(args)
    isvalid = check_numbers(numbers)
    for value in kwargs:
        if value == 'mean':
            if isvalid:
                pass
            else:
                print('ERROR')
        elif value == 'median':
            if isvalid:
                pass
            else:
                print('ERROR')
        elif value == 'quartile':
            if isvalid:
                pass
            else:
                print('ERROR')
        elif value == 'std':
            if isvalid:
                pass
            else:
                print('ERROR')
        elif value == 'var':
            if isvalid:
                pass
            else:
                print('ERROR')
        else:
            pass
