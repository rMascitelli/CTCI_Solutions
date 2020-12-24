# Chapter 1 - Arrays and Strings

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

# 1.6
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

print(stringCompress("aabcccccaaad"))