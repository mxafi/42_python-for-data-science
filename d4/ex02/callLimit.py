def callLimit(limit: int):
    """Decorator factory.

    Returns:
        The decorator.

    """
    count = 0

    def callLimiter(function):
        """Actually the decorator.

        Returns:
            The decorated function.
        """
        def limit_function(*args, **kwds):
            """The decorated function, replaces the original.

            This function is the wrapper, that can run code before and after
            the original function. It is returned by the decorator and
            replaces the original function. It is responsible for calling
            the original function being called.

            Returns:
                The result of the original function if the call count is
                less than the limit, otherwise None.

            """
            nonlocal count
            ident = f"<function {function.__name__} at {hex(id(function))}>"
            if not isinstance(limit, int):
                message = "decorator argument is not an integer"
                print(f"Error: {ident} {message}")
                return
            if count < limit:
                count += 1
                return function(*args, **kwds)
            message = "call too many times"
            print(f"Error: {ident} {message}")
            return
        return limit_function
    return callLimiter
