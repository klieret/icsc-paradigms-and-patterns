class Uncertainty:
    def __init__(self, absolute_errors):
        # construct from absolute errors
    
    @classmethod
    def from_config(cls, config):
        # get absolute errors from config file
        return cls(absolute_errors)
    
    @classmethod
    from relative_errors(cls, data, relative_errors):
        return cls(data * relative_errors) 
 
 
instance = Uncertainty.from_config("path/to/my/config")
