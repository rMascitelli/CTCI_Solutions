# Chapter 1 - Arrays and Strings

A = [[1, 2, 3, 4],
     [5, 6, 0, 8], 
     [9, 10, 11, 12], 
     [13, 3, 15, 16],
     [9, 17, 9, 14]]

# Print a matrix, formatted nicely
def printMatrix(A):
	print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in A]))

# 1.1 - O(n)
def isUnique(input_str):
	hits = [''] * 26
	base = ord('a')

	for c in input_str:
		idx = ord(c) - base

		if(hits[idx] != ''):
			return False
		else:
			hits[idx] = c

	return True

# 1.2 - O(n)
def isPermutation(s1, s2):

	hits = [0] * 26
	base = ord('a')

	if(len(s1) > len(s2)):
		longer = s1
		shorter = s2
	else:
		longer = s2
		shorter = s1

	for c in shorter:
		idx = ord(c) - base
		hits[idx] += 1

	for c in longer:
		idx = ord(c) - base

		if(hits[idx] == 0):
			return False

	return True 

# 1.3 - O(n)
def URLify(input_str, length):

	split = input_str.split(" ")
	url = ""

	for i in range(0, len(split)-1):
		if(split[i] != ""):
			url += str(split[i]) + "%20"

	return url[0:len(url)-3]

# 1.4 - O(n)
def palindromePermutation(input_str):

	# Form a hits[] hash_table as I usually do
	hits = [0] * 26
	base = ord('a')
	odd = (len(input_str) % 2) != 0			

	for c in input_str:
		if(c != ' '):
			hits[ord(c.lower()) - base] += 1

	print(hits)

	# A palindrome needs an even # of chars
	# And an odd number of one char if it's len() is odd (more than one odd hits[] means False)
	num_odd = 0
	for h in hits:
		if((h%2) != 0):
			if(num_odd > 0):
				return False
			else:
				num_odd += 1


	return True

# 1.5 - O(n) worst case, O(1) best case
def oneAway(str_a, str_b):

	hits_a = [0] * 26; hits_b = [0] * 26
	base = ord('a')
	penalty = 0

	# More than 2 difference in length is a short-circuit failure
	if(abs(len(str_a) - len(str_b)) > 1):
		return False

	# Make the hits arrays
	for str_x in [str_a, str_b]:
		for c in str_x:
			if(str_x == str_a):
				hits_a[ord(c) - base] += 1
			else:
				hits_b[ord(c) - base] += 1

	# "oneAway" pairs should have max ONE mismatch in number of each character
	for i in range(0, 26):
		if(hits_a[i] != hits_b[i]):			
			if(penalty < 1):
				# Multiple characters
				if(abs(hits_a[i] - hits_b[i]) > 1):
					return False
				else:
					penalty += 1
			
			else:
				if(len(str_a) != len(str_b)):
					return False
	
	# One letter difference
	if(penalty < 2):
		return True
	else:
		return False

# 1.6 - O(n)
def stringCompress(input_str):

	last_char = ''
	ret_str = ""
	span = 0
	for i in range(0, len(input_str)):
		if(input_str[i] != last_char):
			if(i > 0):
				ret_str += str(last_char) + str(span)

			last_char = input_str[i]
			span = 1

		else:
			span += 1

	ret_str += str(last_char) + str(span)
	return ret_str

# 1.7 - O(n^2)
# TODO: Found this solution online, need to work on finding patterns
# Also struggled with the looping indeces for this one
def rotateMatrix(A):
	"""
        :type A: List[int][int]
        List[x] gives the xth row
    """

	N = len(A[0])

	for i in range(N // 2):
		N = N-1
		for j in range(i, N - i):
			temp = A[i][j]
			A[i][j] = A[N - j][i]
			A[N - j][i] = A[N - i][N - j]
			A[N - i][N - j] = A[j][N - i]
			A[j][N - i] = temp

# 1.8 - O(n^2)
# TODO: is BCR = O(n^2) because we need to check every index? 
def zeroMatrix(A):
	"""
		:type A: List[int][int]
		If one element is 0, the whole row + column should be 0
		For an m x n matrix
	"""

	N = len(A)
	i_zeros = [0] * len(A)				# Hold position of zeros
	j_zeros = [0] * len(A[0])			# Format like a 1:1 hash-map for O(1) lookup time

	for i in range(0, N):
		for j in range(0, len(A[0])):
			if(A[i][j] == 0):
				j_zeros[j] = j
				i_zeros[i] = i

	for i in range(0, N):
		for j in range(0, len(A[0])):
			if(j_zeros[j] != 0 or i_zeros[i] != 0):
				A[i][j] = 0

# 1.9 - O(n)
def stringRotation(str_a, str_b):

	if(str_a == str_b):
		return True
	# They must be the same length
	elif(len(str_a) != len(str_b)):
		return False

	start = None
	found_start = False

	# We need to identify the "rotation point"
	for i in range(0, len(str_b)):

		# Loop through, find str_a[0], and loop until the whole string is found
		if(str_b[i] == str_a[0]):
			#print("Match:", i)
			# Once a match is found, loop through the rest of the string to make sure the rotation point is correct
			for j in range(0, len(str_b)):
				pos = i+j
				if(pos > len(str_b)-1):
					pos = 0 + (pos - len(str_b))
				
				#print(str_b[pos], " =", str_a[j], " ? ")
				if(str_b[pos] != str_a[j]):
					break

				# If we get to the last element, set the start point
				if(j == len(str_b)-1):
					return True

	return False

print("Res =", stringRotation("taterbottlesx", "bottlesxtater"))



