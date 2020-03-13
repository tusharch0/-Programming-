# list with integer elements
list = [10, 20, 10, 30, 10, 40, 10, 50]
# number (n) to be removed
n = 10

# print original list
print("Original list:")
print(list)

# loop to traverse each element in list
# and, remove elements
# which are equals to n
i = 0  # loop counter
length = len(list)  # list length
while(i < length):
	if(list[i] == n):
	list.remove(list[i])
	# as an element is removed
	# so decrease the length by 1
	length = length - 1
	# run loop again to check element
	# at same index, when item removed
	# next item will shift to the left
	continue
	i = i+1

# print list after removing given element
print("list after removing elements:")
print(list)
