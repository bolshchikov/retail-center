class Node:
	def __init__(self, capacity_ = 0):
		self._capacity = capacity_
		self._price = 0
	
	def isLeaf(self):
		'''Should return true if this node has no children, false otherwise'''
		pass
	
	def addChild(self, child):
		'''This method adds child to the node'''
		pass

	def getCapacity(self):
		return self._capacity

	def getPrice(self):
		return self._price

	def setPrice(self, price_):
		self._price = price_