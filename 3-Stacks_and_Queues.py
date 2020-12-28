# Chapter 3 - Stacks and Queues

class Stack:

	def __init__(self, val):
		self.top = val
		self.arr = [val]

	def push(self, push_val):
		self.arr += [push_val]
		self.top = push_val

	def pop(self):
		self.top = self.arr[-2]
		ret = self.arr[-1]
		self.arr = self.arr[:-1]
		return ret

	def peek(self):
		return self.top

	def print(self):
		print("[", end = '')
		for i in self.arr[:-1]:
			print(str(i)+", ", end = '')

		print(str(self.arr[-1])+"]")

	# 3.5 - Sort the smallest items on top of the stack
	# Not allowed to use a temporary array, only a temporary Stack
	def sortStack(self):


class Queue:

	def __init__(self, val):
		self.front = val
		self.arr = [val]

	def enQueue(self, push_val):
		self.arr += [push_val]
		self.top = push_val

	def deQueue(self):
		ret = self.arr[0]
		self.front = self.arr[1]
		self.arr = self.arr[1:]
		return ret

	def print(self):
		print("[", end = '')
		for i in self.arr[:-1]:
			print(str(i)+", ", end = '')

		print(str(self.arr[-1])+"]")

# 3.3
# Suppose the "data" is that each plate has a number
class SetOfStacks:

	def __init__(self, val, max_len):
		self.stacks = [Stack(val)]			# Array of stacks
		self.max_length = max_len

	def push(self, push_val):
		create_new = False
		index = 0

		# Find a stack that hasnt exceeded its max_length
		while(len(self.stacks[index].arr) == self.max_length):
			index += 1

			# Break if there is no next element in stacks[]
			if(len(self.stacks) == index):
				create_new = True
				break

		# Either append a new array to stacks, or append an element to an existing array
		if(create_new):
			self.stacks.append(Stack(push_val))
		else:
			self.stacks[index].push(push_val)

	def pop(self):
		temp = self.stacks[-1]
		return temp.pop()

	# Pop a specific index of plate stacks
	def popAt(self, idx):
		temp = self.stacks[idx]
		return temp.pop()

	def print(self):
		for i in self.stacks:
			i.print()


s = SetOfStacks(5, 2)
s.push(7)
s.push(9)
s.push(11)
s.push(13)
s.push(15)
print(s.popAt(0))
s.push(23)
s.print()



