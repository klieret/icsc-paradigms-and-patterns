# Create path to add modules (=Command objects) to
path = create_path()

# Load data (convenience function that adds a "DataLoader" module to the path)
inputMdstList("default", "/path/to/input/file", path=path)

# Get final state particles

# Fill 'pi+:loose' particle list with all particles that have pion ID > 0.01:
fillParticleList("pi+:loose", "piid > 0.01", path=path)
# Fill 'mu+:loose' particle list with all particles that have muon ID > 0.01:
fillParticleList("mu+:loose", "piid > 0.01", path=path)

# Reconstruct decay
# Fill 'K_S0:pipi' particle list with combinations of our pions and muons
reconstructDecay(
	"K_S0:pipi -> pi+:loose pi-:loose", "0.4 < M < 0.6", path=path
)

# Process path = call execute() on all Command objects
process(my_path)
