import ROOT


def fill_tree(treeName, fileName):
    tdf = ROOT.ROOT.RDataFrame(10)
    tdf.Define("data", "(double) tdfentry_")\
       .Define("theory", "tdfentry_ + 0.1")\
       .Define("error", "0.1").Snapshot(treeName, fileName)

# We prepare an input tree to run on
fileName = "df001_introduction_py.root"
treeName = "myTree"
fill_tree(treeName, fileName)

rdf = ROOT.ROOT.RDataFrame(treeName, fileName)

print(rdf)

rdf = rdf.Filter("!(data==theory & error==0.)").Define("sqd", "pow(data-theory, 2) / pow(error, 2)")
chi2 = rdf.Sum("sqd").GetValue()

print(chi2)
