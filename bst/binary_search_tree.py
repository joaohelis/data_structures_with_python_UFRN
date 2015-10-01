from search_and_sort import merge_sort
from stack_queue.stack_algorithm import stack_algorithm

class Node(object):
    
    value = None
    parent = None
    left = None
    right = None
    
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        
    def __str__(self):
        value = str(None if self.value == None else self.value)
        parent = str(None if self.parent == None else self.parent.value)
        left = str(None if self.left == None else self.left.value)
        right = str(None if self.right == None else self.right.value)
        return 'Node [value='+value+' parent='+parent+' left='+left+' right='+right+']'
        
        

class BinarySearchTree(object):
    
    root = None
    size = None
    
    def make_BST_aux(self, list, l, u, parent):
        if l <= u:
            m = (l+u)/2
            node = Node(list[m])
            node.parent = parent
            node.left = self.make_BST_aux(list, l, m-1, node)
            node.right = self.make_BST_aux(list, m+1, u, node)
            return node
        return None
    
    def make_BST(self, list):
        merge_sort.merge_sort(list)
        return self.make_BST_aux(list, 0, len(list)-1, None)
    
    def __init__(self, list_elements=None):
        self.size = 0
        if list_elements != None:
            self.root = self.make_BST(list_elements)
            self.size = len(list_elements)
    
    def search_recursive_aux(self, node, element):
        if node == None or node.value == element:
            return node
        else:
            if element < node.value:
                return self.search_recursive_aux(node.left, element)
            else:
                return self.search_recursive_aux(node.right, element)
            
    def minimum_aux(self, node):
        if node == None or node.left == None:
            return node
        else:
            return self.minimum_aux(node.left)
        
    def maximum_aux(self, node):
        if node == None or node.right == None:
            return node
        else:
            return self.maximum_aux(node.right)
        
    def maximum(self):
        return self.maximum_aux(self.root)
    def minimum(self):
        return self.minimum_aux(self.root)
            
    def search(self, element, node=None):
        if node == None:
            node = self.root
        return self.search_recursive_aux(node, element)
    
    def search_iterative(self, element, node=None):
        if node == None:
            node = self.root
        it = node
        while it != None and it.value != element:
            if element < it.value:
                it = it.left
            else:
                it = it.right
        return it
    
    def next(self, node):
        if node.right != None:
            return self.minimum_aux(node.right)
        else:
            next = node.parent
            while next != None and node == next.right:
                node = next
                next = next.parent
            return next
        
    def prev(self, node):
        if node.left != None:
            return self.maximum_aux(node.left)
        else:
            prev = node.parent
            while prev != None and node == prev.left:
                node = prev
                prev = prev.parent
            return prev
    
    def in_order(self, node, list):
        if node != None:
            self.in_order(node.left, list)
            list.append(node.value)
            self.in_order(node.right, list)
    
    def print_in_order(self, node):
        if node != None:
            self.print_in_order(node.left)
            print node
            self.print_in_order(node.right)
            
    def __str__(self):
        list = []
        self.in_order(self.root, list)
        return str(list)
            
    def in_order_iterative(self, node):
        if node != None:
            visited = []
            stack = stack_algorithm.Stack()
            stack.push(node)
            while not(stack.empty()):                
                while node.left != None:
                    stack.push(node.left)
                    node = node.left
                node = stack.pop()
                if not(node in visited):
                    print node
                visited.append(node)
                while node.right != None:
                    stack.push(node.right)
                    node = node.right
    
    def insert_aux(self, value, node, parent):
        if node == None:
            new_node = Node(value, parent, None, None)
            if parent != None:
                if value < parent.value:
                    parent.left = new_node
                else:
                    parent.right = new_node
        else:
            if value < node.value:
                self.insert_aux(value, node.left, node)
            else:
                self.insert_aux(value, node.right, node)
            
    def insert(self, value):
        self.insert_aux(value, self.root, None)
        self.size += 1
            
    def is_leaf(self, node):
        return node != None and node.left == None and node.right == None
    
    def has_left(self, node):
        return node != None and node.left != None
    
    def has_right(self, node):
        return node != None and node.right != None
    
    def swap_values_between_nodes(self, node_one, node_two):
        aux = node_one.value
        node_one.value = node_two.value
        node_two.value = aux
        
    def remove(self, value):
        element_to_remove = self.search(value, self.root)
        if element_to_remove != None:
            self.remove_aux(element_to_remove)
            self.size -= 1
            
    def remove_aux(self, element_to_remove):
        if element_to_remove != None:
            if self.is_leaf(element_to_remove): # folha
                if element_to_remove.parent != None:
                    if element_to_remove.parent.left == element_to_remove:
                        element_to_remove.parent.left = None
                    else:
                        element_to_remove.parent.right = None
            elif self.has_left(element_to_remove) and self.has_right(element_to_remove):
                min_right = self.minimum_aux(element_to_remove.right)
                self.swap_values_between_nodes(element_to_remove, min_right)
                self.remove_aux(min_right)
            elif self.has_left(element_to_remove):
                if element_to_remove.parent.left == element_to_remove:
                    element_to_remove.parent.left = element_to_remove.left
                    element_to_remove.left.parent = element_to_remove.parent
                else:
                    element_to_remove.parent.right = element_to_remove.left
                    element_to_remove.left.parent = element_to_remove.parent
            else:
                if element_to_remove.parent.left == element_to_remove:
                    element_to_remove.parent.left = element_to_remove.right
                    element_to_remove.right.parent = element_to_remove.parent 
                else:
                    element_to_remove.parent.right = element_to_remove.right
                    element_to_remove.right.parent = element_to_remove.parent              
        
    def __len__(self):
        return self.size

"""
bst = BinarySearchTree([0, 1, float(1.5), 2, 3, 4, 5, 6, 7, 8, 9])
bst.insert(10)
bst.insert(20)
bst.insert(-10)
print 'bst_in_order =',bst
print 'remove (5)'
bst.remove(5)
print 'bst_in_order =',bst
print 'search (10) =',bst.search(10)
print 'minimum =', bst.minimum()
print 'maximum =', bst.maximum()
print 'next (0) =',bst.next(bst.search(0))
print 'prev (6) =',bst.prev(bst.search(6))
"""