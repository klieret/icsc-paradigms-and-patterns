# Create path to add modules to
my_path = create_path()

# Adding modules to path:

# Load data from ROOT file:
inputMdst(filename="input.root", path=my_path)
# Get final state particles and put them in a particle list:
fillParticleListsFromMC([("gamma", ...), ("pi-", ...), ...], path=my_path)
# Reconstruct pi0 -> gamma gamma:
ma.reconstructDecay(
	decayString='pi0 -> gamma gamma', 
	cut='0.1 < InvM < 0.15',
    path=my_path
)
# Write NTuple output file:
variablesToNtuple(..., path=my_path)

# Process path:
process(my_path)
