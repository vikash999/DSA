class Node():
	def __init__(self,data):
		self.data =data
		self.next = None

class Linkedlist():
	def __init__(self):
		self.head =None


	def push(self,new_data):
		new_node =Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def printlist(self):
		temp = self.head
		while(temp):
			print(temp.data,end=' ')
			temp = temp.next

if __name__=="__main__":
	llist = Linkedlist()
	llist.push(1)
	llist.push(2)
	llist.push(3)
	llist.printlist()
