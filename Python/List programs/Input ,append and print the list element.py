# declare a list
list = []

# read limit (value of n)
# for maximum number of elements
n = int(input("Enter limit of the list: "))

# input n integer element
# and append to the list
for i in range(n):
	item = int(input("Enter an integer: "))
	list.append(item)

# print all elements
print "Input list elements are: "
for i in range(n):
	print list[i]
