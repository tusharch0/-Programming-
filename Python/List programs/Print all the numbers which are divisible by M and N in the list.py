# declare a list of integers
list = [10, 15, 20, 25, 30]

# declare and assign M and N
M = 3
N = 5

# print the list
print "List is: ", list

# Traverse each element and check
# whether it is divisible by M, N
# or not, if condition is true print
# the element
print "Numbers divisible by {0} and {1}".format(M, N)
for num in list:
	if(num % M == 0 and num % N == 0):
	print num
