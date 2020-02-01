# Using std python
def chi2(data, theory, data_errors):
	err_sum = 0
	for i in range(len(data)):
		err_sum += (data[i] - theory[i])**2 / (data_errors[i]**2)
	return err_sum


# Using pandas dataframes
chi2 = (df["data"] - df["theory"]).pow(2) / df["data_errors"].pow(2)).sum()
