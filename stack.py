class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

reversed_list = ''
stack = Stack()
for a in "helllo":
   stack.push(a)
for a in range (len(stack.items)):
    reversed_list += stack.pop()

print(reversed_list)    