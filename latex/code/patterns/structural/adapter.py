class OurMLModel(ABC):
	""" Our interface """
	@abstractmethod
	def train(...):
		pass


class TheirMLModel(ABC):
	""" Their interface """
	@abstractmethod
	def training(...)  # <-- this method should be called train
		pass


class ModelAdapter(OurMLModel):  # <-- implements our interface
	def __init__(self, model: TheirMLModel):
		self._model = model   # <-- our adapter holds the foreign model

	def train(...):           # <-- and defines a different interface for it
		self._model.training(...)


# Their model with our interface:
model = ModelAdapter(TheirMLModel(...))  # (actually need TheirConcreteMLModel)

