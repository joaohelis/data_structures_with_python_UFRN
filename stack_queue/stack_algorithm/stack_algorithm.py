class StackException(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return repr(self.msg)

class Stack(object):
    
    stack, max, size = None, None, None
    
    def __init__(self, max=10):
        self.max = max
        self.size = 0
        self.stack = [None for element in range(max)]
    
    def empty(self):
        return self.size == 0
    
    def full(self):
        return self.size == self.max
        
    def push(self, element):
        if self.full(): 
            raise StackException('The stack is full!')
        self.stack[self.size] = element
        self.size += 1
        
    def top(self):
        if self.empty():
            raise StackException("Cannot access the stack top, because the stack's empty!")
        return self.stack[self.size - 1]
    
    def pop(self):
        if self.empty():
            raise StackException("The stack is empty!")
        removed_element = self.stack[self.size - 1]
        self.size -= 1
        return removed_element
        
    def __str__(self):
        return str(self.stack[:self.size])
          
## TEST

"""
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(50)
        
print stack
print stack.size

print stack.pop()
print stack

"""