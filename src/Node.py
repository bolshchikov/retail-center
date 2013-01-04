class Node:
	def __init__(self, capacity_ = 0):
		self._capacity = capacity_
		self._price = 0
		self._children = []
		self._path = []
		self._exprectation = None
		self.next = None
	
	def isLeaf(self):
		'''Should return true if this node has no children, false otherwise'''
		return True if self._capacity == 0 else False
	
	def addChild(self, child):
		'''This method adds child to the node'''
		self._children.append(child)

	def getChildren(self):
		return self._children

	def getCapacity(self):
		return self._capacity

	def reduceCapacity(self, value):
		self._capacity -= value		

	def getPrice(self):
		return self._price

	def setPrice(self, price_):
		self._price = price_

	def addToPath(self, node):
		self._path = node.getPath() + [node]

	def getPath(self):
		return self._path

	def setExpectation(self, value):
		self._exprectation = value

	def getExpectation(self):
		return self._exprectation