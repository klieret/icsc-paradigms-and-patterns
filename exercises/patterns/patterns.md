# Exercises - patterns

### Counter example for LSP

### DIP 

### Factory method

Perhaps easier example: Temperature scales or take form lecture. 

```python
# Use example from lecture, implement mock methods
# e.g. random (true random), pseudorandom: always 1, from file: hardcoded or hash of filename
```



### Builder pattern

Matplotlib example: Several hlines, vlines, plots

```python
import matplotlib.pyplot as plt

class ComplexPlot(object):
    def __init__(self, datasets, datasetcolors, datalabels, hlines, vlines, hlinecolors, vlinecolors):
    	self.datasets = datsets
        self.datasetcolors = datasetcolors
        self.datalabels = datalabels
        self.hlines = hlines
        self.vlines = vlines
        self.hlinecolors = hlinecolors
        self.vlinecolors = vlinecolors
    
    def plot():
        fig, ax = plt.subplots()
        for i in range(len(self.datasets)):
            ax.plot(self.datasets[i], color=self.datasetcolors[i], label=self.datalables[i])
        for i in range(len(self.hlines)):
            ax.axhline(self.hlines[i], color=self.hlinecolors[i])
        for i in range(len(self.vlines)):
            ax.axhline(self.vlines[i], color=self.vlinecolors[i])
        ax.legend()
        return ax
       
```

```python
# Solution

class ComplexPlot(object):
    def __init__(self):
    	self.datasets = []
        self.datasetcolors = []
        self.datalabels = []
        self.hlines = []
        self.vlines = []
        self.hlinecolors = []
        self.vlinecolors = []
    
    def add_dataset(data, color="black", label=""):
        self.datasets.append(data)
        self.datasetcolors.append(color)
        self.datalabels.append(label)
    
    def add_hline(y, color="black"):
        self.hlines.append(y)
        self.hlinecolors.append(color)
    
    def add_vline(y, color="black"):
        self.hlines.append(y)
        self.hlinecolors.append(color)
    
    def plot():
        # Same as before
        fig, ax = plt.subplots()
        for i in range(len(self.datasets)):
            ax.plot(self.datasets[i], color=self.datasetcolors[i], label=self.datalables[i])
        for i in range(len(self.hlines)):
            ax.axhline(self.hlines[i], color=self.hlinecolors[i])
        for i in range(len(self.vlines)):
            ax.axhline(self.vlines[i], color=self.vlinecolors[i])
        ax.legend()
        return ax
```

```python
# Solution

class ComplexPlot(object):
    def __init__(self):
    	self.datasets = []
        self.datakwargs = []
        self.hlines = []
        self.vlines = []
        self.hlinekwargs = []
        self.vlinekwargs = []
    
    def add_dataset(data, **kwargs):
        self.datasets.append(data)
        self.datasetkwarts.append(kwargs)
    
    def add_hline(y, **kwargs):
        self.hlines.append(y)
        self.hlinekwargs.append(kwargs)
    
    def add_vline(y, **kwargs):
        self.hlines.append(y)
        self.hlinecolors.append(kwargs)
    
    def plot():
        fig, ax = plt.subplots()
        for i in range(len(self.datasets)):
            ax.plot(self.datasets[i], **self.datasetkwargs)
        for i in range(len(self.hlines)):
            ax.axhline(self.hlines[i], **self.hlinekwargs)
        for i in range(len(self.vlines)):
            ax.axhline(self.vlines[i], **self.vlinekwargs)
        ax.legend()
        return ax
```



### Adapter 

