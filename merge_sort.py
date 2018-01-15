def merge_sort(A):
	if len(A) > 1:
		A1 = merge_sort(A[:len(A) / 2])
		A2 = merge_sort(A[len(A) / 2: len(A)])
		return merge(A1, A2)
	return A

def merge(A1, A2):
	B = []
	i = 0
	j = 0
	for _ in range(len(A1) + len(A2)):
		if i < len(A1) and (j >= len(A2) or A1[i] < A2[j]):
			B.append(A1[i])
			i += 1
		else:
			B.append(A2[j])
			j += 1
	return B

A = [1, 3, 2, 4, 10, 1]
print merge_sort(A)