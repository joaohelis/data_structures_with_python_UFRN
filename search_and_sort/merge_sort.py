def merge(A, B, l, m, u):
	i = 0
	j = l
	k =  m + 1
	while(j <= m and k <= u):
		if(A[j] < A[k]):
			B[i] = A[j]
			j += 1
			i += 1
		else:
			B[i] = A[k]
			k += 1
			i += 1
	while(j <= m):
		B[i] = A[j]
		j += 1
		i += 1
	while(k <= u):
		B[i] = A[k]
		k += 1
		i += 1
	for i in range(l, u + 1):
		A[i] = B[i - l]

def merge_sort_aux(A, B, l, u):
	if(l < u):
		m = (int) (l + (u - l) / 2)
		merge_sort_aux(A, B, l, m)
		merge_sort_aux(A, B, m+1, u)
		merge(A, B, l, m, u)
	return A

def merge_sort(A):
	B = [None for x in range(len(A))]
	return merge_sort_aux(A, B, 0, len(A)-1)


"""
## MAIN ##

A = [2, 8, 7, 1, 100, 2, 30, 4, 1000, 20, 2, 0, -1, 7,3]
merge_sort(A)
print A
"""