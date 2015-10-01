
""" 1) Eh ppossivel implementar as funcionalidades de fila utilizando
       pilha(s)? Se sim, como? Se nao, por que?"""

from stack_queue.queue import queue_algorithm
from stack_queue.stack_algorithm import stack_algorithm

class Queue_With_Stack(object):
    
    stack = None
    stack_aux = None
    max = None
    
    def __init__(self, max=10):
        self.stack = stack_algorithm.Stack()
        self.stack_aux = stack_algorithm.Stack()
        self.max = max
        
    def empty(self):
        return self.stack.empty()
    
    def full(self):
        return self.stack.full()
    
    def size(self):
        return self.stack.size
    
    def enqueue(self, element):
        self.stack.push(element)
        
    def head(self):
        while not(self.stack.empty()):
            self.stack_aux.push(self.stack.pop())
        head = self.stack_aux.top()
        while not(self.stack_aux.empty()):
            self.stack.push(self.stack_aux.pop())
        return head

    def dequeue(self):
        while not(self.stack.empty()):
            self.stack_aux.push(self.stack.pop())
        removed_element = self.stack_aux.pop()
        while not(self.stack_aux.empty()):
            self.stack.push(self.stack_aux.pop())
        return removed_element
        
    def __str__(self):
        return str(self.stack)



""""Eh possivel implementar as funcionalidades de pilha utilizando
    fila(s)? Se sim, como? Se nao, por que?"""
        
class Stack_With_Queue(object):
    
    queue = None
    queue_aux = None
    max = None
    
    def __init__(self, max=10):
        self.queue = queue_algorithm.Queue(max)
        self.queue_aux = queue_algorithm.Queue(max)
        self.max = max
        
    def size(self):
        return self.queue.size
        
    def push(self, element):
        self.queue.enqueue(element)
    
    def top(self):
        while self.queue.size > 1:
            self.queue_aux.enqueue(self.queue.dequeue())
        top_element = self.queue.dequeue()
        self.queue_aux.enqueue(top_element)
        self.queue = self.queue_aux
        self.queue_aux = queue_algorithm.Queue(self.max)
        return top_element
    
    def pop(self):
        while self.queue.size > 1:
            self.queue_aux.enqueue(self.queue.dequeue())
        top_element = self.queue.dequeue()
        self.queue = self.queue_aux
        self.queue_aux = queue_algorithm.Queue(self.max)
        return top_element
    
    def __str__(self):
        return str(self.queue)