def insertion_sort(A):
	for j in range(1, len(A)):
		key = A[j]
		i = j - 1
		while(i >= 0 and A[i] > key):
			A[i + 1] = A[i]
			i -= 1
		A[i + 1] = key
	return A

def recursive_insertion_sort(A, j):
	if j < len(A):
		key = A[j]
		i = j - 1
		while(i >= 0 and A[i] > key):
			A[i + 1] = A[i]
			i -= 1
		A[i + 1] = key
		recursive_insertion_sort(A, j + 1)
	return A

def insertion_sort_02(A):
	return recursive_insertion_sort(A, 2)

"""
A = [2, 8, 7, 1, 100, 2, 30, 4, 1000, 20, 2, 0, -1, 7,3]
print insertion_sort_02(A)
"""