import pytest
import numpy as np
from circ_queue import Queue

def test_queue_simple():
    q = Queue(5)
    assert len(q.data) == 5
    assert isinstance(q.data, np.ndarray)

    for i in range(5):
        q.enqueue(i)
        
    with pytest.raises(RuntimeError):
        q.enqueue(5)

    for i in range(5):
        assert q.dequeue() == i
        
    assert q.empty()

def test_queue_circularity():
    q = Queue(10)

    for i in range(6):
        q.enqueue(i)
    
    assert len(q.data) == 10
    assert sum([1 for x in q.data if x is None]) == 4

    for i in range(5):
        q.dequeue()
        
    assert not q.empty()
    assert q.head == q.tail
    assert q.head == 5

    for i in range(9):
        q.enqueue(i)

    with pytest.raises(RuntimeError):
        q.enqueue(10)

    for x, y in zip(q, [5] + list(range(9))):
        assert x == y
        
    assert q.dequeue() == 5
    for i in range(9):
        assert q.dequeue() == i

    assert q.empty()

def test_queue_resize():
    q = Queue(5)
    for i in range(5):
        q.enqueue(i)
    for i in range(4):
        q.dequeue()
    for i in range(5, 9):
        q.enqueue(i)
        
    with pytest.raises(RuntimeError):
        q.enqueue(10)

    assert len(q.data) == 5

    q.resize(10)

    assert len(q.data) == 10
    assert isinstance(q.data, np.ndarray)

    for x, y in zip(q, range(4, 9)):
        assert x == y
        
    for i in range(9, 14):
        q.enqueue(i)

    for i in range(4, 14):
        assert q.dequeue() == i
        
    assert q.empty()
    assert q.head == -1
