def sum_squares_to(n, partial_sum=0):
    if n == 0:
        return partial_sum
    return sum_up_to(n-1, partial_sum + n^2)
