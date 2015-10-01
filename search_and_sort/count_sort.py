
def count_sort_aux(A, B, k):
	C = [0 for x in range(k + 1)]

	for i in range(0, len(A)):
		C[A[i]] = C[A[i]] + 1

	for i in range(1, k + 1):
		C[i] = C[i] + C[i - 1]

	for i in range(len(A)-1, -1, -1):
		B[C[A[i]]-1] = A[i]
		C[A[i]] = C[A[i]] - 1

	return B

def count_sort(A):
	B = [None for x in range(len(A))]
	k = max(A)
	return count_sort_aux(A, B, k)

"""
A = [2, 8, 7, 1, 100, 2, 30, 4, 1000, 20, 2, 0, 7,3, 1, 0]

print count_sort(A)
"""

