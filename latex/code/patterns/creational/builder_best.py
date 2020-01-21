class Data:
    pass

class Builder:
    def __init__(...)
    
    def add_mc_component(...)
    
    def create(...) -> Data


builder = Builder(...)
builder.add_mc_component(...)
...
builder.add_mc_component(...)
data = builder.create()
