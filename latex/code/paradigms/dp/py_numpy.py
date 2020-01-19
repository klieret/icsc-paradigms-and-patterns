def chi2(vec_a, vec_b, err_a):
    return math.sqrt(sum([(a-b)**2/err_a for a, b in zip(vec_a, vec_b)]))
