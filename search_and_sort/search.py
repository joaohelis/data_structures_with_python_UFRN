
## Search Algorithms

def binary_search_iterative(A, v):
	l = 0
	u = len(A)
	m = l + (u - l) / 2
	while A[m] != v and l < u:
		if v < A[m]:
			u = m - 1
		else:
			l = m + 1
		m = l + (u - l) / 2
	if(A[m] == v):
		return m
	else:
		return -1

def binary_search_recursive(A, v, l, u):
	if l > u:
		return -1;
	m = (int) (l + (u - l)/2)
	if A[m] == v:
		return m;
	elif A[m] > v:
		return binary_search_recursive(A, v, l, m-1);
	else:
		return binary_search_recursive(A, v, m+1, u);

def binary_search(A, v):
	return binary_search_recursive(A, v, 0, len(A))

def linear_search(A, v):
	for i in range(0, len(A)):
		if A[i] == v:
			return i
	return -1

def linear_search_to_ordered_list(A, v):
	i = 0
	while i < len(A) and A[i] < v:
		i += 1
	if i < len(A) and A[i] == v:
		return i
	else:
		return -1


"""
# == main

A = [1, 2, 5, 50, 60, 80, 100]

print binary_search(A, 50)
"""