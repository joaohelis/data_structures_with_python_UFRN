class QueueException(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return repr(self.msg)
    
class Queue(object):
    
    queue = None
    head = None
    tail = None
    size = None
    max = None
    
    def __init__(self, max=3):
        self.head = 0
        self.tail = -1
        self.size = 0
        self.max = max
        self.queue = [None for element in range(max)]
        
    def empty(self):
        return self.size == 0
    
    def full(self):
        return self.size == self.max
    
    def head(self):
        if self.empty(): 
            raise QueueException('The queue is empty...')
        return self.queue[self.head]
    
    def enqueue(self, element):
        if self.full():
            raise QueueException('The queue is full...')
        self.tail = (self.tail + 1) % self.max
        self.queue[self.tail] = element
        self.size += 1
          
    def dequeue(self):
        if self.empty():
            raise QueueException('The queue is empty...')
        removed_element = self.queue[self.head]
        self.head = (self.head + 1) % self.max
        self.size -= 1
        return removed_element
        
    def __str__(self):
        if self.empty(): return '[]'
        else:
            string = ''
            it = self.head
            count = 0
            while count < self.size:
                string += str(self.queue[it]) + ', '
                it = (it + 1) % self.max
                count += 1
            return '['+string[:-2]+']'
        
## TEST

"""
queue = Queue()

print 'queue', queue, 'size:', queue.size, 'head:', queue.head, 'tail:', queue.tail

print 'enqueue: 10'
print 'enqueue: 20'
print 'enqueue: 50'
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(50)

print 'queue', queue, 'size:', queue.size, 'head:', queue.head, 'tail:', queue.tail

print 'dequeue:', queue.dequeue()
print 'dequeue:', queue.dequeue()
print 'queue', queue, 'size:', queue.size, 'head:', queue.head, 'tail:', queue.tail

"""
