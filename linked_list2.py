class Node:
	def __init__(self, data, next= None):
		self.data = data
		self.next = next

class Linked_list:
	def __init__(self):
		self.head = None

	def append_node(self, data):
		if not self.head: 
			self.head = Node(data)
		else: 
			current = self.head
			while  current.next:
				current = current.next
			current.next = Node(data)


	def print_linked_list(self):  	
		node = self.head 

		while node:
			print(node.data)
			node = node.next


OUR_LIST = Linked_list()

OUR_LIST.append_node("Sunday")
OUR_LIST.append_node("Monday")
OUR_LIST.append_node("Thuesday")
OUR_LIST.append_node("Wednesday")


OUR_LIST.print_linked_list()




