# Chapter 2 - Linked Lists

class Node:

	def __init__(self, val):
		self.val = val
		self.next = None

class LinkedList:

	def __init__(self, val):
		self.head = Node(val)

	def add(self, val):
		temp = self.head
		while(temp.next != None):
			temp = temp.next

		temp.next = Node(val)

	def print(self):
		temp = self.head
		print("[" + str(temp.val) + "] -> ", end='')

		while(temp.next != None):
			temp = temp.next
			print("(" + str(temp.val) + ") -> ", end='')

		print("End")


	# 2.1
	def removeDups(self):

		if(self.head.next):
			temp = self.head.next
		else:
			return

		prev = self.head
		hits = [0] * 100	# Assuming max length is 100, not a good assumption
		hits[self.head.val] += 1

		while(temp.next != None):
			#print("prev =", prev.val, ", cur =", temp.val, ", next =", temp.next.val, end='')
			save = temp.val						# TODO: may not need to save this value

			# Found a match, replace the link beteen prev and next
			if(hits[temp.val] > 0):
				#print("  (Replacement made)")
				prev.next = prev.next.next
				temp = temp.next
			else:
				prev = temp 					# Keep a reference to 'prev' to replace duplicates
				temp = temp.next
				#print(" ")

			hits[save] += 1							# Create a hit list
			
		# TODO: Should be able to do this within the initial loop I think
		if(hits[temp.val] > 0):
			prev.next = temp.next

	# 2.2
	def kthToLast(self, k):

		temp = self.head
		kth_ago = None
		itr = 1

		while(temp.next):
			# Once we see at least 'k' elements
			if(itr >= k):
				# Set 'kth_ago' to self.head (start of LL)
				if(itr == k):
					kth_ago = self.head
				# Or start incrementing kth_ago as we continue to increment
				else:
					kth_ago = kth_ago.next

			itr += 1
			temp = temp.next

		print(kth_ago.val)

	# 2.3
	def deleteMiddleNode(self, node):

		delete_val = node.val
		prev = self.head
		temp = self.head.next

		# Simply look for the delete_val and remove that 'link'
		# Starting from head.next means first element wont be deleted
		# Looping structure means last element wont be deleted
		while(temp.next):
			if(delete_val == temp.val):
				prev.next = temp.next
				return

			temp = temp.next
			prev = prev.next

	# 2.4 is super confusing
	# 2.5
	def sumLists(self, list_b, op):

		# Debug print info
		print("/*   Adding:")
		self.print()
		list_b.print()
		print("*/")

		accum = 0
		itr = 0
		carry_over = 0
		f_head_carry_over = False
		a = self.head
		b = list_b.head

		# Values are stored in reverse orders
		if(op == 'r'):
			while(a or b):
				if(a == None):
					accum = b.val + carry_over
				elif(b == None):
					accum = a.val + carry_over
				else:
					accum = a.val + b.val + carry_over

				if(accum >= 10):
					carry_over = accum // 10
				else:
					carry_over = 0

				#print(itr, ":", accum, "% 10 =", accum%10)

				if(itr == 0):
					ret = LinkedList(accum%10)
				else:
					ret.add(accum%10)
				
				a = a.next if (a != None) else None
				b = b.next if (b != None) else None
				itr += 1

			if(carry_over):
				ret.add(carry_over)

		# TODO: Currently 'f' only supports same length lists
		# Can add extra cases, but need to decide how these cases should be handled
		elif(op == 'f'):
			while(a or b):

				if(itr == 0):
					if(a.val + b.val >= 10):
						f_head_carry_over = 1

				# First check for carry-over
				if(a.next and b.next):
					#print('[{0}]: a: {1}, b: {2}'.format(itr, a.next.val, b.next.val))
					if((a.next.val + b.next.val) >= 10):
						carry_over = 1
					else:
						carry_over = 0
				else:
					carry_over = 0

				# Set the 'accum' value for this iteration
				if(a == None):
					accum = b.val + carry_over
				elif(b == None):
					accum = a.val + carry_over
				else:
					accum = a.val + b.val + carry_over

				if(itr == 0):
					ret = LinkedList(accum%10)
				else:
					ret.add(accum%10)

				a = a.next if (a != None) else None
				b = b.next if (b != None) else None
				itr += 1

			if(f_head_carry_over):
				n = LinkedList(f_head_carry_over)
				n.head.next = ret.head
				ret = n

		else:
			print("Invalid operation! Check 'op' parameter")
			return

		return ret

	# 2.6
	def palindrome(self):
		temp = self.head
		vals = []

		# Log all values in our array
		while(temp):
			vals += [temp.val]
			temp = temp.next

		# Iterate top and bottom until we find a mismatch (if possible)
		top = 1
		for i in range(0, len(vals)):
			if(vals[i] != vals[-top]):
				return False
			top += 1

		return True

	# 2.7 would require more implementation in the LL class
	# Not a question, just Floyd's Loop Detection using 2-pointer
	def isLoop(self):
		slow = self.head
		fast = self.head.next

		while(fast and fast.next):
			print("slow=", slow.val, "fast=", fast.val)
			if(fast.val == slow.val):
				return True

			fast = fast.next.next
			slow = slow.next

	# 2.8
	def loopDetection(self):
		temp = self.head
		hits = [False] * 5000		# Should be sys.maxint

		while(temp):
			if(hits[temp.val]):
				return temp.val
			hits[temp.val] = True
			temp = temp.next

		return None


t = LinkedList(1)
t.add(2)
t.add(3)
t.add(4)
t.add(5)
t.add(6)
t.print()
r = LinkedList(7)
r.add(9)
r.add(5)
#r.add(4)
#t.sumLists(r, 'f').print()
#print(t.palindrome())	
print(t.loopDetection())
