import math

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
		'''
		Algorithm should check that the amount of leaves of a current node is less than node's 
		capacity. As well as check that leaf's amount is also less than capacity of every node 
		on a path. E.g. if amount of leaves is 5, and capacity of parent node is 6, it's OK. 
		However, if a capacity of grand node is 2, then the demand cannot be answered.
		Complexity is O(nlogn)
		'''

		#debugging
		# string = ''
		# for i in root.getPath():
		# 	string += str(i.getCapacity()) + ' '
		# print string

		num = 0										# amount of leaves
		root.addToPath(root)						# add node itself to the path for future comparison
		for node in root.getChildren():				# count amount of leaves or save path to node
			node.addToPath(root)
			if node.isLeaf():
				num += 1
		root.getPath()[0].reduceCapacity(num)

		if root.getPath()[0].getCapacity() < 0:
			return 0

		for i in range(2, len(root.getPath())):		# for every node in the path, compare node's capacity											# to amount of leaves	
			if num > root.getPath()[i].getCapacity():
				return 0
		for node in root.getChildren():				#recursive call for each child node
			if self.canDemandBeAnswered(node) == 0:
				return 0
		return 1


	def maxLeaf(self, leaf1, leaf2):
		if leaf1.getPrice() > leaf2.getPrice():
			return leaf1
		else: 
			return leaf2


	def getBestCustomers(self, root):
		'''
		This method should return a linked list of nodes representing the 
		customers with the overall highest revenue.
		The resulting list should conform to the capacity limitations.
		'''
		
		answer = None # pointer to the head of the linked list

		q = [root]
		while q:
			v = q.pop(0)
			for node in v.getChildren():
				if node.isLeaf():
					if min(v.getExpectation(), v.getCapacity()) == 1:
						maxLeaf = self.maxLeaf(v.getChildren()[0], v.getChildren()[1])
						if answer == None:
							answer = maxLeaf
						else:
							maxLeaf.next = answer
							answer = maxLeaf
						break
					else:
						if answer == None:
							answer = node
						else:
							node.next = answer
							answer = node			
				else:
					q = q + [node]
					node.setExpectation(int(math.ceil(v.getCapacity()/2)))
		return answer
					

	def printTree(self, root):
		'''Tree printing for debug purposes'''
		printStr = str(root.getCapacity()) + ' -> '
		for node in root.getChildren():
			printStr += str(node.getCapacity()) + ' '
		print printStr
		for node in root._children:
			self.printTree(node)