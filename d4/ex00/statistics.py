def check_numbers(numbers: list) -> bool:
    """Check if the numbers are valid"""
    if not numbers:
        return False
    for number in numbers:
        if not isinstance(number, (int, float)):
            return False
    return True


def print_res(type: str, res: int | float | list[int | float]) -> None:
    """Print the results in the desired format"""
    if isinstance(res, list) and len(res) == 0:
        return
    print(f"{type} : {res}")


def ft_mean(numbers: list) -> float:
    """Calculate the mean of a given list of numbers"""
    res = sum(numbers) / len(numbers)
    return res


def ft_median(numbers: list) -> float:
    """Calculate the median of a given list of numbers. (sorts the list)"""
    numbers.sort()
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    return ft_mean([numbers[n // 2 - 1], numbers[n // 2]])


def ft_quartile(numbers: list) -> list:
    """Calculate the 25% and 75% quartiles of a given list of numbers"""
    # Sort and split the list
    if len(numbers) < 4:
        print('ERROR')
        return []
    numbers.sort()
    n = len(numbers)
    res25 = ft_median(numbers[:n // 2])
    res75 = ft_median(numbers[n // 2 + n % 2:])
    return [res25, res75]


def ft_variance(numbers: list) -> float:
    """Calculate the variance of a given list of numbers."""
    mean = ft_mean(numbers)
    res = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return res


def ft_std(numbers: list) -> float:
    """Calculate the standard deviation of a given list of numbers."""
    return ft_variance(numbers) ** 0.5


def ft_statistics(*args, **kwargs) -> None:
    """Calculate and print common statistics for a given list of numbers.

    Args:
        *args: Variable length argument list of numbers.
        **kwargs: Arbitrary keyword arguments. Supported any=type where type:
            - 'mean': Calculate and print the mean of the numbers.
            - 'median': Calculate and print the median of the numbers.
            - 'quartile': Calculate and print the quartile of the numbers.
            - 'std': Calculate and print the standard deviation of the numbers.
            - 'var': Calculate and print the variance of the numbers.

    Error:
        If the numbers are invalid, prints 'ERROR'
        for each supported kwargs type.

    Returns:
        None

    """
    numbers = list(args)
    isvalid = check_numbers(numbers)
    for key in kwargs:
        value = kwargs[key]
        match value:
            case 'mean':
                if isvalid:
                    print_res(value, ft_mean(numbers))
                else:
                    print('ERROR')
            case 'median':
                if isvalid:
                    print_res(value, ft_median(numbers))
                else:
                    print('ERROR')
            case 'quartile':
                if isvalid:
                    print_res(value, ft_quartile(numbers))
                else:
                    print('ERROR')
            case 'std':
                if isvalid:
                    print_res(value, ft_std(numbers))
                else:
                    print('ERROR')
            case 'var':
                if isvalid:
                    print_res(value, ft_variance(numbers))
                else:
                    print('ERROR')
            case _:
                pass
