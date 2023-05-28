import numpy as np
from typing import Any


class Queue:
    def __init__(self, limit=10):
        self.data = np.empty(limit, dtype=object)
        self.head = -1
        self.tail = -1
        self.count = 0

    
    def empty(self):
        return self.count == 0


    def __bool__(self):
        return not self.empty()
   

    def __str__(self):
        if not(self):
            return ''
        return ', '.join(str(x) for x in self)
    

    def __repr__(self):
        return str(self)
    
   
    ## Don't change the above code!
    
    def enqueue(self, val: Any):
        raise NotImplementedError


    def dequeue(self) -> Any:
        raise NotImplementedError


    def resize(self, newsize: int):
        assert len(self.data) < newsize
        raise NotImplementedError


    def __iter__(self):
        raise NotImplementedError
