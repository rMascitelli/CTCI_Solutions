# Chapter 5 - Bit Manipulation

# Helper function to print binary values to 16 bits, with padding
def bprint(value):
	print(format(value, '08b'))

# Helper function to find the longest span of 1's
def span(value):
	span = 0; longest = 0
	num_bits = len(bin(value)[2:])

	for n in range(0, num_bits+1):
		if(value & (1 << n)):						# If we find a 1, increase span
			span += 1
		else:								# If we find a 0, set "longest" and reset span
			if(span > longest):
				longest = span
			span = 0

	return longest

# Helper function to flip bits from index i - j
def flipBits(value, i, j):

	#print("i=", i, "j=", j)
	#print("orig:", end=''); bprint(value)

	left = (1 << (j+1)) - 1
	right = (1 << i) - 1
	mask = left & ~right

	# Use mask to clear bits on value, and set bits on temp
	ret = value & ~mask
	temp = ~value & mask

	ret |= temp
	#print("fin :", end=''); bprint(ret)
	return ret

# 5.1
def insertion(N, M, i, j):
	bn = bin(N)
	bm = bin(M)

	print("Inserting", bn, "<<", bm, "-- i=", i, ", j=", j)
	ret = ~0

	# First clear bits i to j in N
	left = (1 << (i+1)) - 1
	right = (1 << j) - 1
	mask = left & ~right
	ret = ~mask & N

	# Then shift and OR (M << j)
	bprint(ret | (M << j))
	return ret | (M << j)

# 5.3 - O(n^2) where n = # of bits in value
def flipBitToWin(value):
	print("Finding longest span:", end=''); bprint(value)
	bin_val = bin(value)[2:]				# String to represent binary stream (take out leading 0b)
	longest = 0

	for i in range(0, len(bin_val)):

		# If we find a 0, replace with 1 and loop through the num to find longest span
		if(bin_val[-(1+i)] == "0"):
			temp = value | (1 << i)

			if(span(temp) > longest):
				longest = span(temp)

	return longest

# 5.4 - O(n)
def nextNumber(value):

	# Loop through to find first occurrence of "01" and "10"
	# We will then swap these bits to find bigger and smaller next numbers
	num_bits = len(bin(value)[2:])
	smaller = None; bigger = None
	for i in range(0, num_bits):
		# "10" found
		if(not(value & (1 << i)) and (value & (1 << (i+1))) and smaller == None):
			smaller = i

		# "01" found
		if((value & (1 << i)) and not(value & (1 << (i+1))) and bigger == None):
			bigger = i

	# With smaller/bigger index, we want to swap bits (i, i+1)
	#print("bigger=", bigger, "smaller=", smaller)

	# Now use flipBits() with bigger/smaller as parameters to get final answer
	ret_b = flipBits(value, bigger, bigger+1)
	ret_s = flipBits(value, smaller, smaller+1)

	print("ret_b: ", end=''); bprint(ret_b); print("(", ret_b, ")")
	print("ret_s: ", end=''); bprint(ret_s); print("(", ret_s, ")")

	return (ret_b, ret_s)

#insertion(213, 15, 6, 3)
#bprint(213)
#print("longest = ", flipBitToWin(221))

x = 13
bprint(x)
nextNumber(x)