def quick_sort(A, l, r):
	if l < r:
		A, q = partition(A, l, r)
		A = quick_sort(A, l, q - 1)
		A = quick_sort(A, q + 1, r)
	return A
	

def partition(A, l, r):
	x = A[r]
	i = l - 1

	for j in range(l, r):
		if A[j] <= x:
			i += 1
			A[i], A[j] = A[j], A[i]

	A[i + 1], A[r] = A[r], A[i + 1]

	return A, i + 1

A = [1, 3, 2, 4, 10, 1]
print quick_sort(A, 0, len(A) - 1)