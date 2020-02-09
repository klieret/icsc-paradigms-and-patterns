def sum_squares_to(n):
    return 0 if n == 0 else n^2 + sum_squares_to(n-1)
