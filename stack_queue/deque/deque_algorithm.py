from dns.name import empty

class DequeException(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return repr(self.msg)

class Deque(object):
    
    deque = None
    head = None
    tail = None
    size = None
    max = None
    
    def __init__(self, max=10):
        self.size = 0
        self.max = max
        self.head = 0
        self.tail = -1
        self.deque = [None for element in range(max)]
        
    def empty(self):
        return self.size == 0
    
    def full(self):
        return self.size == self.max
    
    def front(self):
        if self.empty():
            raise DequeException('The deque is empty...')
        return self.deque[self.head]
    
    def back(self):
        if self.empty():
            raise DequeException('The deque is empty...')
        return self.deque[self.tail]
        
    def push_front(self, element):
        if self.full():
            raise DequeException('The deque is full...')
        if self.head == 0:
            self.head = self.size - 1
        else:
            self.head -= 1
        self.deque[self.head] = element
        
    def push_back(self, element):
        if self.full():
            raise DequeException('The deque is full...')
        self.tail = (self.tail + 1) % self.max
        self.deque[self.tail] = element
        
    def pop_front(self):
        if self.empty():
            raise DequeException('The deque is empty...')
        self.head = (self.head + 1) % self.max     