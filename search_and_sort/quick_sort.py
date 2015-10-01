def swap(A, i, j):
	aux = A[i]
	A[i] = A[j]
	A[j] = aux

def partition(A, l, u):
	pivot = A[l]
	i = l
	j = u

	while True:
		while A[i] <= pivot and i < u:
			i += 1
		while A[j] > pivot:
			j -= 1
		if i < j:
			swap(A, i, j)
		else:
			swap(A, j, l) # swap j with pivot
			return j

def quick_sort_aux(A, l, u):
	if l < u:
		m = partition(A, l, u)
		quick_sort_aux(A, l, m -1)
		quick_sort_aux(A, m + 1, u)
	return A

def quick_sort(A):
	return quick_sort_aux(A, 0, len(A)-1)

"""
## MAIN ##

A = [2, 8, 7, 1, 100, 2, 30, 4, 1000, 20, 2, 0, -1, 7,3]
print quick_sort(A)
"""