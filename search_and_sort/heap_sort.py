class Heap(object):
	
	def __init__(self):
		self.heap = []

	def swap(self, A, i, j):
		aux = A[i]
		A[i] = A[j]
		A[j] = aux

	def up(self, i):
		return (int) (i / 2)

	def left(self, i):
		return i * 2 + 1

	def right(self, i):
		return (i * 2) + 2

	def sift_up(self, HEAP, i):
		if self.up(i) >= 0 and HEAP[i] > HEAP[self.up(i)]:
			self.swap(HEAP, i, self.up(i))
			self.sift_up(HEAP, self.up(i))

	def sift_down(self, HEAP, i, size=None):
		if(size == None):
			size = len(HEAP)
		if self.left(i) > size -1:
			return
		elif self.left(i) == size -1:
			if HEAP[i] < HEAP[self.left(i)]:
				self.swap(HEAP, i, self.left(i))
		else:
			bigger_son = self.left(i) if HEAP[self.left(i)] >= HEAP[self.right(i)] else self.right(i)
			if HEAP[i] < HEAP[bigger_son]:
				self.swap(HEAP, i, bigger_son)
				self.sift_down(HEAP, bigger_son, size)

	def build_heap(self, A=None):
		if A is None:
			A = self.heap
		i = (len(A)- 1) / 2
		while i >= 0:
			self.sift_down(A, i)
			i -= 1
		return A

	def get_max(self):
		return self.heap[0]

	def set_heap(self, heap):
		self.heap = self.build_heap(heap)

	def size(Self):
		return len(self.heap)
	 
	def insert(self, v, HEAP=None):
		if HEAP == None:
			HEAP = self.heap
		self.heap.append(v)
		self.sift_up(HEAP, len(HEAP) -1)

	def remove_max(self, HEAP=None):
		if HEAP == None:
			HEAP = self.heap
		HEAP[0] = HEAP[len(HEAP) - 1]
		del HEAP[len(HEAP) -1]
		self.sift_down(HEAP, 0)

	def heap_sort(self, HEAP=None):
		if HEAP == None:
			HEAP = [element for element in self.heap]
		else:
			self.build_heap(HEAP)
		for size in range(len(HEAP) -1, 0, -1):
			self.swap(HEAP, 0, size)
			self.sift_down(HEAP, 0, size)
		return HEAP

"""
## MAIN TEST ##

heap = Heap()

heap.insert(50)
heap.insert(1)
heap.insert(25)
heap.insert(30)
heap.insert(0)
heap.remove_max()
heap.remove_max()
print heap.heap
print heap.heap_sort()

A = [2, 8, 7, 1, 100, 2, 30, 4, 1000, 20, 2, 0, -1, 7,3]
print heap.heap_sort(A)
"""