class ft_filter:
    """
    ft_filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable
    for which function(item) is true.
    If function is None, return the items that are true.
    """
    def __init__(self, function, iterable):
        self.__function = function
        self.__iterable = iterable
        self.__index = 0
        self.__result = []

        if not hasattr(iterable, "__iter__"):
            iterable_type = type(iterable)
            raise TypeError(f"'{iterable_type.__name__}'"
                            " object is not iterable")

        if self.__function is not None and not callable(self.__function):
            return None

        for item in self.__iterable:
            if self.__function is None:
                if item:
                    self.__result.append(item)
            else:
                if function(item):
                    self.__result.append(item)

    def __iter__(self):
        if self.__function is not None and not callable(self.__function):
            function_type = type(self.__function)
            raise TypeError(f"'{function_type.__name__}'"
                            " object is not callable")
        for item in self.__result:
            yield item

    def __repr__(self):
        return f"<ft_filter object at {hex(id(self))}>"
