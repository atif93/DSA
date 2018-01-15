import math

class maxheap(object):

	def __init__(self):
		self.arr = []

	def parent(self, key):
		return int(math.floor((key - 1) / 2))

	def children(self, key):
		return 2 * key + 1, 2 * key + 2

	def heapify(self, key):
		children = self.children(key)
		if children[0] < len(self.arr):
			maxkey = children[0]
			if children[1] < len(self.arr) and self.arr[children[1]] > self.arr[maxkey]:
				maxkey = children[1]
		elif children[1] < len(self.arr):
			maxkey = children[1]
		else:
			return

		if self.arr[maxkey] > self.arr[key]:
			self.arr[maxkey], self.arr[key] = self.arr[key], self.arr[maxkey]
			self.heapify(maxkey)


	def insert(self, val):
		self.arr.append(val)

		key = len(self.arr) - 1
		while self.parent(key) >= 0 and self.arr[key] > self.arr[self.parent(key)]:
			self.arr[key] = self.arr[self.parent(key)]
			key = self.parent(key)
			self.arr[key] = val

	def max(self):
		return self.arr[0]

	def extract_max(self):
		max = self.max()

		self.arr[0] = self.arr[len(self.arr) - 1]
		del self.arr[-1]

		self.heapify(0)

		return max

	def build_heap(self, arr):
		self.arr = arr
		key = self.parent(len(arr) - 1)

		for i in range(key, -1, -1):
			self.heapify(i)

	def k_largest(self, k):
		kmax = []
		
		for i in range(k):
			kmax.append(self.extract_max())

		return kmax


mh = maxheap()
mh.insert(2)
mh.insert(4)
mh.insert(1)
print mh.arr


mh.build_heap([9, 8, 6, 12, 14])
print mh.arr
print mh.k_largest(5)
print mh.arr