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

print(URLify("testa ton rest     ", 15))
