
class Node(object):
	def __init__(self, value=None, next=None):
		self.value = value
		self.next = next

	def __str__(self):
	    return "Node [value="+str(self.value)+" next="+str(self.next.value)+"]"

class LinkedList(object):

	def __init__(self, head=None):
		self.head = head
		self.size = 0

	def insert_end(self, value):
		newNode = Node(value)
		if self.size == 0:
			self.head = newNode
		else:
			it = self.get(self.size - 1)
			newNode.next = it.next
			it.next = newNode
		self.size += 1

	def insert_ordered(self, value):
		newNode = Node(value)
		it = self.head
		beforeElement = None

		if self.head == None or value <= self.head.value:
			newNode.next = self.head
			self.head = newNode
		else:
			while True:
				beforeElement = it
				it = it.next
				if it == None or it.value >= value:
					break
			newNode.next = it
			beforeElement.next = newNode
		self.size += 1


	def remove_by_index(self, index):
		if index >= self.size:
			print "Throw exception!"
		if self.size == 1:
			self.head = None
		elif index == 0:
			self.head = self.head.next
		else:
			it = self.get(index - 1)
			it.next = it.next.next
		self.size -= 1

	def search(self, value):
		it = self.head
		index_of_element = 0
		
		while it != None and it.value != value:
			index_of_element += 1
			it = it.next

		return index_of_element if (it != None and it.value == value) else -1

	def search_ordered(self, value):
		it = self.head
		index_of_element = 0
		while it != None and it.value < value:
			index_of_element += 1
			it = it.next

		return index_of_element if (it != None and it.value == value) else -1

	def remove_ordered(self, value):
		if self.head == None:
			return -1
		
		returnValue = -1
		if self.head.value == value:
			self.head = self.head.next
			returnValue = 0
		else:
			it = self.head			
			beforeElement = None
			index_of_element = 0
			
			while True:
				beforeElement = it
				it = it.next
				index_of_element += 1
				if beforeElement.next == None or beforeElement.next.value >= value:
					break

			if beforeElement.next != None and beforeElement.next.value == value:
				beforeElement.next = it.next
				returnValue = index_of_element

		if returnValue >= 0 and returnValue < self.size:
			self.size -= 1

		return returnValue

	def remove(self, value):
		if self.size == 0:
			return -1
		
		returnValue = -1
		if self.head.value == value:
			self.head = self.head.next
			returnValue = 0
		else:
			it = self.head			
			beforeElement = None
			index_of_element = 0
			
			while True:
				beforeElement = it
				it = it.next
				index_of_element += 1
				if beforeElement.next == None or beforeElement.next.value == value:
					break

			if index_of_element < self.size:
				beforeElement.next = it.next
				returnValue = index_of_element

		if returnValue >= 0 and returnValue < self.size:
			self.size -= 1

		return returnValue

	def get(self, index):
		if index > self.size - 1:
			print "Throw exception!"
		node = self.head
		for it in range(index):
			node = node.next
		return node

	def __str__(self):
		
		to_string = "["

		it = self.head
		while(it != None):
			to_string += str(it.value) +", "
			it = it.next

		to_string = to_string[:-2] + "]" if self.size > 0 else "[]"
		return to_string


"""
linkedList = LinkedList()

linkedList.insert_end(1)
linkedList.insert_end(2)
linkedList.insert_end(3)
linkedList.insert_end(30)
linkedList.insert_end(40)
linkedList.insert_end(100)

print linkedList
print 'search_ordered (40) =',linkedList.search_ordered(40)
print 'size =', linkedList.size, '\n'

print 'remove (30)'
linkedList.remove(30)
print linkedList
print 'size =', linkedList.size
"""