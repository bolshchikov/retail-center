class HW4:

	'''
	You are to implement the two functions in this class.
	You can add any other method or members to it as well.
	However, you cannot change their signature. 
	'''
	def canDemandBeAnswered(self, root):
		'''
		This method will return true if the tree rooted at node sn can answer
		the demand induced by its leaves.
		'''
		num = 0
		for node in root.getChildren():
			if node.isLeaf():
				num += 1
		if num > root.getCapacity():
			return 0
		for node in root.getChildren():
			return self.canDemandBeAnswered(node)
		return 1


	def getBestCustomers(self, root):
		'''
		This method should return a linked list of nodes representing the 
		customers with the overall highest revenue.
		The resulting list should conform to the capacity limitations.
		'''
		pass 

	def printTree(self, root):
		'''Tree printing for debug purposes'''
		printStr = str(root.getCapacity()) + ' -> '
		for node in root.getChildren():
			printStr += str(node.getCapacity()) + ' '
		print printStr
		for node in root._children:
			self.printTree(node)