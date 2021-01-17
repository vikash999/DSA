class node():
	def __init__(self,data):
		self.data =data
		self.next = None

class linkedlist():
	def __init__(self):
		self.head = None
	# at the bignning 
	def push(self,new_data):
		new_node = node(new_data)
		
		new_node.next = self.head
		self.head = new_node
		
	def delete_list(self):
		temp = self.head
		while(temp):
			prev = temp.next
			del (temp.data)
			temp = prev


	def printlist(self):
		temp = self.head
		while(temp!=None):
			print(temp.data,end=' ')
			temp = temp.next

if __name__=="__main__":
	llist = linkedlist()
	llist.push(1)
	llist.push(2)
	llist.push(3)
	
	llist.printlist()
	print()

	llist.delete_list()
	
