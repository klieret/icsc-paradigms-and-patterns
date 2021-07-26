def get_map_function(function):
    """ Takes a function f and returns the function map(f, *) """
    def _map_function(iterator):
        return map(function, iterator)

    return _map_function


mf1 = get_map_function(lambda x: x**2)
mf2 = get_map_function(lambda x: x+1)

mf2(mf1([1, 2, 3]))
>>> [2, 5, 10]
