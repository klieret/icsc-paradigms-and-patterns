def map(function, iterator):
    """ Our own version of map (returns a list rather than a generator) """
    return [function(item) for item in iterator]


map(lambda x: x**2, [1, 2, 3])
>>> [1, 4, 9]
