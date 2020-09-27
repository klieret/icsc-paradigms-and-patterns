# Exercises Functional Programming

## Resources

* [1] https://anandology.com/python-practice-book/functional-programming.html

## Memoization

* Apply to fib and note that we now get linear runtime/a linearly growing callgraph.

## Recursion

* Fibonacci
* Head vs tail recursion
* Loop to recursion

## Higher order functions

### Classic examples


```python
# vectorize: Take a function that only takes scalars; 
# returns a function that also takes iterable 

def vectorize(fct):
	""" """

	def vectorized(lst):
        if isinstance(lst, Iterable):
			return [fct[item] for item in lst]
		else:
            return fct(lst)
        
	return vectorized
```

```python
def composite(fcts):
	""" Returns composition of list of functions"""
    
    def comp(inpt):
        for fct in fcts:
            inpt = fct(inpt)
        return inpt
    
    return comp
```

```python
# Recursion + higher level function
# Treemap (like map, but handling nested lists)

def treemap(fct, nested_list):
    """ """
    
    if not isinstance(nested_list, list):
        return fct(nested_list)
    else:
        return [treemap(fct, lst) for lst in nested_list]
```

### Using HOF to configure behavior

```python

```

* Fitting: Dynamic number of bins
* Plotting: plot fct
* ML: ML Model?



* Could simply do this: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html

### Using HOF for logging; decorators

```python
import time

def log_call(fct):
    
    def _logged_fct(*args, **kwargs):
        return_value = fct(*args, **kwargs)
        print(f"{fct.__name__}({args}, {kwargs}) = {return_value}")
       
    return _logged_fct


@log_call
def fib(n):
    pass
```

+Follow up: Add timing.

+ Follow up: Apply to fibonacci function using ``fib = log_call(fib)``

## OOP

### Inheritance

Factor out common code by introducing a class to inherit from, e.g. child, parent with greet method. Make it subclass of person.

