"""
Map Function 
	Syntax: map(function, iterable)
	Applies function to every item of the iterable
"""

def triple(n):
	return n * 3

# numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
numbers = range(0, 16)

# tripled_numbers = []

# for number in numbers:
# 	tripled_numbers.append(triple(number))

tripled_numbers = map(triple, numbers)

print(list(tripled_numbers))