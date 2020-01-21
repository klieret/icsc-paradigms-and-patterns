class Uncertainty:
    def __init__(self, absolute_errors=None,  relative_error=None, 
        data=None, config=None, ...):
        if config is not None:
            # load from config
        elif absolute_errors is not None:
            # add absolute errors
        elif relative_errors is not None and data is not None:
            # add relative errors  
        ...


instance = Uncertainty(config="path/to/my/config")
