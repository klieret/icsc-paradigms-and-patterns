def sum_squares_to(n, partial_sum=0):
    return partial_sum if n == 0 else sum_squares_to(n-1, partial_sum + n^2)
