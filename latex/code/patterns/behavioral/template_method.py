class MLModel(ABC):  # <-- abstract class
	def load_data(...)
	def prepare_features(...)

	@abstractmethod
	def train(...):
		pass

	def validate(...)
	...


class BDT(MLModel):  # <-- concrete class
	def train(...):
		# Implementation


class RandomForest(MLModel):
	def train(...):
		# Implementation
