class MyAnalysis(): 
	def __init__(ml_model: MLModel, fitter: Fitter)
        self.ml_model = ml_model
        self.fitter = fitter
    
    def fit(...):
        self.fitter.fit(...)
    
    def train(...):
        self.ml_model.train(...)

class MLModel(ABC):
    @abstractmethod
    def train(...)

class RandomForest(MLModel):
	def train(...):
		# Implementation


my_analysis = MyAnalysis(RandomForest(...), KernelDensityEstimator(...))
my_analysis.train(...)
my_analysis.fit(...)
