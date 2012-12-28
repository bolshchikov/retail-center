import Node
import HW4


def part1():
	hw4 = HW4()
	#failing scenario
	s8 = Node(8)
	s5 = Node(5)
	s6 = Node(6)
	for i in range(2):
		s6.addChild(Node())
	
	s7 = Node(7)
	s2 = Node(2)
	for i in range(3):
		s2.addChild(Node())

	s3 = Node(3)
	s2_2 = Node(2)   
	s2_2.addChild(Node())
	
	s4 = Node(4)
	for i in range(5):
		s4.addChild(Node())
	
	
	s1 = Node(1)
	for i in range(2):
		s1.addChild(Node())      
	
	s2_3 = Node(2)
	for i in range(4): 
		s2_3.addChild(Node())
	
	s2_4 = Node(2)  
	for i in range(3):
		s2_4.addChild(Node())
	
	s8.addChild(s5)
	s8.addChild(s6)    
	s5.addChild(s7)
	s5.addChild(s2)
	s6.addChild(s3)
	s6.addChild(s2_2)
	s7.addChild(s4)
	s7.addChild(s1)
	s3.addChild(s2_3)
	s3.addChild(s2_4)
	ans = hw4.canDemandBeAnswered(s8)
	print ' ans= %d' % ans
	
	#successfull scenario
	s2_15 = Node(15)
	s2_8 = Node(8)
	s2_12 = Node(12)  
	s2_15.addChild(s2_8)
	s2_15.addChild(s2_12)
	
	for i in range(2): 
		s2_12.addChild(Node())
	
	
	s2_7 = Node(7)        
	s2_21 = Node(2) 
	for i in range(2): 
		s2_21.addChild(Node())
									
	s2_6 = Node(6)
	for i in range(2): 
		s2_6.addChild(Node())
		
	s2_8.addChild(s2_7)
	s2_8.addChild(s2_21)
	s2_12.addChild(s2_6)
	
	s2_24 = Node(4)            
	for i in range(3): 
		s2_24.addChild(Node())
	
	
	s2_22 = Node(2)    
	for i in range(2): 
		s2_22.addChild(Node())
							
	s2_5 = Node(5)  
	for i in range(4): 
		s2_5.addChild(Node())
						 
	s2_7.addChild(s2_24)
	s2_7.addChild(s2_22)
	s2_6.addChild(s2_5)
	ans = hw4.canDemandBeAnswered(s2_15)
	print ' ans= %d' % ans
	return 0

def part2():
	hw4 = HW4()
	#failing scenario
	s7 = Node(7)
	s4 = Node(4)
	s3 = Node(3)
	s2_1 = Node(2)
	s2_2 = Node(2)
	s2_3 = Node(2)
	s1_1 = Node(1)
	s1_2 = Node(1)
	s1_3 = Node(1)
	s1_4 = Node(1)
	l81 = Node()
	l81.setPrice(81)
	l70 = Node()
	l70.setPrice(70)
	l20 = Node()
	l20.setPrice(20)
	l92 = Node()
	l92.setPrice(92)
	l11 = Node()
	l11.setPrice(11)
	l13 = Node()
	l11.setPrice(13)
	l57 = Node()
	l57.setPrice(57)
	l93 = Node()
	l93.setPrice(93)
	l80 = Node()
	l80.setPrice(80)
	l25 = Node()
	l25.setPrice(25)
	l80_1 = Node()
	l80_1.setPrice(80)
	s7.addChild(s4)
	s7.addChild(s3)
	s4.addChild(s2_1)
	s4.addChild(s1_1)
	s3.addChild(l57)
	s3.addChild(s2_2)
	s2_1.addChild(s1_2)
	s2_1.addChild(s1_3)
	s1_1.addChild(l11)
	s1_1.addChild(l13)
	s2_2.addChild(s1_4)
	s2_2.addChild(s2_3)
	s1_2.addChild(l81)
	s1_2.addChild(l70)
	s1_3.addChild(l20)
	s1_3.addChild(l92)
	s1_4.addChild(l93)
	s1_4.addChild(l80)
	s2_3.addChild(l25)
	s2_3.addChild(l80_1)
	bestCusts = hw4.getBestCustomers(s7)
	print 'highest priced customers: '
	t = bestCusts
	while t != None:
		print t.getPrice()
		t = t.next

def main():
	part1()
	part2()

if __name__=='__main__':
	main()