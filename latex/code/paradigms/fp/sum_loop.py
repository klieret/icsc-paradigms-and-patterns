def sum_squares_to(n):
    result = 0
    for i in range(n+1):
        result += i^2
    return result
