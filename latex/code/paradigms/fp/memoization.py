import time
from functools import lru_cache


@lru_cache()
def expensive(x):
    time.sleep(1)
    return x+42


%time expensive(2)
>>> Wall time: 1 s

% time expensive(2)
>>> Wall time: 6.2 µs
