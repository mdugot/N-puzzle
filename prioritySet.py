from heapq import heappush, heappop

class PrioritySet:
	def __init__(self):
		self.dict = dict([])
		self.queue = []

	def pop(self):
		while self.queue:
			e = heappop(self.queue)
			if e.deleted == False:
				return e
		return None
	
	def push(self, e):
		if hash(e) in self.dict:
			old = self.dict[hash(e)]
			if e < old:
				old.deleted = True
				self.dict[hash(e)] = e
				heappush(self.queue, e)
		else:
			self.dict[hash(e)] = e
			heappush(self.queue, e)

	def __len__(self):
		return len(self.queue)
