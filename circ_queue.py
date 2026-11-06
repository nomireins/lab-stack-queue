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
        if self.count == len(self.data):
            self.resize(2 * len(self.data))
        if self.empty():
            self.head = self.tail = 0
        else:
            self.tail = (self.tail + 1) % len(self.data)
        self.data[self.tail] = val
        self.count += 1

    def dequeue(self) -> Any:
        if self.empty():
            raise IndexError("queue is empty")
        val = self.data[self.head]
        self.head = (self.head + 1) % len(self.data)
        self.count -= 1
        return val


    def resize(self, newsize: int):
        assert len(self.data) < newsize
        newdata = np.empty(newsize, dtype=object)
        for i in range(self.count):
            newdata[i] = self.data[(self.head + i) % len(self.data)]

    def __iter__(self):
        for i in range(self.count):
            yield self.data[(self.head + i) % len(self.data)]
