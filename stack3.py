class Stack:
	''' afaf '''
	def __init__(self):
		self.items = []

	def push(self, item):
		return self.items.append(item)

	def pop (self):
		return self.items.pop()
		
normal_list = [1, 2, 3, 4, 5]
reversed_list = [0, 0, 0, 0, 0]

STACK = Stack()

for a in normal_list:
    STACK.push(a)

for a in range (len(normal_list)):
    reversed_list[a] = STACK.pop()
print(reversed_list)