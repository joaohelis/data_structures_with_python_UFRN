

class LinkedListException(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return repr(self.msg)

class Node(object):
    
    value = None
    next = None
    
    def  __init__(self, value = None, next = None):
        self.value = value
        self.next = next
    
    def __str__(self):
        return '[value='+ str(self.value) + 'next='+ (str(None) if self.next == None else str(self.next.value)) +']'
    

class SimplyCircularLinkedList(object):
    
    head = None
    size = None
    
    def __init__(self):
        self.size = 0
        
    def get_node_by_index(self, index):
        if index < 0 or index >= self.size:
            raise LinkedListException('Index out of bounds...')
        it = self.head
        for i in range(index):
            it = it.next
        return it 
            
    def get(self, index):
        return self.get_node_by_index(index).value
    
    def empty(self):
        return self.size == 0
        
    def insert_end(self, element):
        newNode = Node(element)
        if self.head == None:
            newNode.next = newNode
            self.head = newNode
        else:
            last_element = self.get_node_by_index(self.size - 1)
            newNode.next = last_element.next
            last_element.next = newNode
        self.size += 1
        
    def insert_begin(self, element):
        newNode = Node(element)
        if self.head == None:
            newNode.next = newNode
            self.head = newNode
        else:
            newNode.next = self.head
            last_element = self.get_node_by_index(self.size - 1)
            last_element.next = newNode
            self.head = newNode
        self.size += 1
        
    def insert_ordered(self, element):
        newNode = Node(element)
        if self.head == None:
            newNode.next = newNode
            self.head = newNode
        else:
            it = self.head
            if self.size == 1:
                if self.head.value > element:
                    self.head.next = newNode
                    newNode.next = self.head
                    self.head = newNode
                else:
                    newNode.next = self.head.next
                    self.head.next = newNode                    
            else:
                while it.next.value < element and it.next != self.head:
                    it = it.next
                newNode.next = it.next
                it.next = newNode
        self.size += 1
          
    def remove_by_index(self, index):
        if index < 0 or index >= self.size:
            raise LinkedListException('Index out of bounds...')
        if index == 0:
            last_element = self.get_node_by_index(self.size - 1)
            self.head = self.head.next
            last_element.next = self.head
        else:
            before_element = self.get_node_by_index(index - 1)
            before_element.next = before_element.next.next
        self.size -= 1
        
    def remove_begin(self):
        self.remove_by_index(0)
        
    def remove_end(self):
        self.remove_by_index(self.size - 1)
        
    def remove(self, element):
        index_of_removed_element = -1
        if not(self.empty()):
            if self.head.value == element:
                if self.size == 1:
                    self.head = None
                else:
                    last_element = self.get_node_by_index(self.size - 1)
                    self.head = self.head.next
                    last_element.next = self.head
                index_of_removed_element = 0
            else:
                before_element = self.head
                while before_element.next.value != element and before_element.next != self.head:
                    before_element = before_element.next
                    index_of_removed_element += 1
                if before_element.next.value == element:
                    before_element.next = before_element.next.next
            self.size -= 1
        return index_of_removed_element
    
    def find(self, element):
        it = self.head
        index = 0
        while it.value != element and it.next != self.head:
            it = it.next
            index += 1
        return -1 if (it.value != element) else index
    
    def find_ordered(self, element):
        it = self.head
        index = 0
        while it.value < element and it.next != self.head:
            it = it.next
            index += 1
        return -1 if (it.value != element) else index
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        if self.head == None: 
            return '[]'
        else:
            string = ''
            it = self.head
            while True:
                string += str(it.value) + ', '
                it = it.next
                if it == self.head:
                    break
            return '['+ string[:-2] + ']'
            
           
"""
linked_list = SimplyCircularLinkedList()

linked_list.insert_end(10)
linked_list.insert_end(20)
linked_list.insert_end(50)
linked_list.insert_begin(1)
linked_list.insert_begin(0)
linked_list.insert_ordered(100)
linked_list.insert_ordered(10)
linked_list.insert_ordered(55)
print linked_list
print linked_list.remove(20)
print linked_list
"""