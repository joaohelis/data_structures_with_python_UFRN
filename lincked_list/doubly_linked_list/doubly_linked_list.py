

class LinkedListException(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return repr(self.msg)
    
class Node(object):
    
    value = None
    next = None
    prev = None
    
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
        
    def __str__(self):
        return 'Node [value='+str(self.value)+' next='+str(None if self.next == None else self.next.value)+' prev='+str(None if self.prev == None else self.prev.value)+']'
    

class DoublyLinkedList(object):
    
    head = None
    size = None
    
    def __init__(self):
        self.size = 0
        
    def get_node_by_index(self, index):
        if index < 0 or index > self.size - 1:
            raise LinkedListException('Index out of bounds...')
        it = self.head
        for i in range(index):
            it = it.next
        return it
    
    def get_node_by_value(self, value):
        index = 0
        it = self.head
        while it != None and it.value != value:
            it = it.next
            index += 1
        return -1 if it == None else index 
        
    def insert_end(self, element):
        new_element = Node(element)
        if self.head == None:
            new_element.next = None
            new_element.prev = None
            self.head = new_element
        else:
            last_element = self.get_node_by_index(self.size - 1)
            new_element.next = None
            new_element.prev = last_element
            last_element.next = new_element
        self.size += 1
        
    def insert_begin(self, element):
        new_element = Node(element)
        if self.head == None:
            new_element.next = None
            new_element.prev = None
            self.head = new_element
        else:
            self.head.prev = new_element
            new_element.prev = None
            new_element.next = self.head
            self.head = new_element
        self.size += 1
        
    def insert_ordered(self, element):
        new_element = Node(element)
        
        index_to_insert = 0
        it = self.head
        before_element = it.prev
        
        while it != None and it.value < element:
            before_element = it
            it = it.next
            index_to_insert += 1
            
        if index_to_insert == 0:
            new_element.prev = None
            new_element.next = self.head
            self.head.prev = new_element
            self.head = new_element
        elif index_to_insert == self.size:
            new_element.next = None
            new_element.prev = before_element
            before_element.next = new_element
        else:
            new_element.next = before_element.next
            new_element.prev = before_element
            before_element.next = new_element
        
        self.size +=1
        
    def remove_by_index(self, index):
        if index < 0 or index > self.size - 1:
            raise LinkedListException('Index out of bounds...')
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        else:
            element_to_remove = self.get_node_by_index(index)
            if index == self.size - 1:
                element_to_remove.prev.next = None
            else:
                element_to_remove.prev.next = element_to_remove.next
                element_to_remove.next.prev = element_to_remove.prev
        self.size -= 1
        
    def __len__(self):
        return self.size
    
    def __str__(self):
        if self.head == None:
            return '[]'
        else:
            string = ''
            it = self.head
            while it != None:
                string += str(it.value)+', '
                it = it.next
            return '['+string[:-2]+']'
        
    
linked_list = DoublyLinkedList()

linked_list.insert_end(10)
linked_list.insert_end(20)
linked_list.insert_end(100)
linked_list.insert_begin(1)

linked_list.insert_ordered(200)
linked_list.insert_ordered(15)
linked_list.insert_ordered(17)

print linked_list
print linked_list.remove_by_index(2)
print linked_list
    