class Uncertainty:
    def __init__(self, absolute_errors):
        # construct from absolute errors

    @classmethod  # <-- doesn't need instance to be called (cf. first slide)
    def from_config(cls, config):
        # get absolute errors from config file
        return cls(absolute_errors)

    @classmethod
    def relative_errors(cls, data, relative_errors):
        return cls(data * relative_errors)


instance = Uncertainty.from_config("path/to/my/config")
