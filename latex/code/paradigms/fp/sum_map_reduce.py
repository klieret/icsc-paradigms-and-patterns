from functools import map, reduce


def sum_squares_to(n):
    return reduce(
        lambda x, y: x+y,
        map(lambda x: x**2, range(n+1))
    )
