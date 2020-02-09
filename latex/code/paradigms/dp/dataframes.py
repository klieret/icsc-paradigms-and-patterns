# "Chi2 distance" using plain python
def chi2(data, theory, error):
	err_sum = 0
	for i in range(len(data)):
		if data[i] == theory[i] and error[i] == 0:
			continue
		err_sum += (data[i] - theory[i])**2 / (error[i]**2)
	return err_sum


# Using DataFrames: Table contains columns experiment, theory, error

# ROOT RDataFrame example:
chi2 = ROOT.ROOT.RDataFrame(...)  # initialize
		.Filter("!(data==theory & error==0.)")  # filter rows
        .Define("sqd", "pow(data-theory, 2) / pow(error, 2)")  # new col
        .Sum("sqd").GetValue()  # sum it up

# Pandas example:
chi2 = pd.DataFrame(...)  # initialize
_df = df.query("~(data==theory & error==0)")  # filter
chi2 = (_df["data"] - _df["theory"]).pow(2) / _df["error"].pow(2)).sum()
