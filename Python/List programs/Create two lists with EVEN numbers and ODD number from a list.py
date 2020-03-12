# declare and assign list1
list1 = [11, 22, 33, 44, 55]

# declare listOdd - to store odd numbers
# declare listEven - to store even numbers
listOdd = []
listEven = []

# check and append odd numbers in listOdd
# and even numbers in listEven
for num in list1:
	if num % 2 == 0:
	listEven.append(num)
	else:
	listOdd.append(num)

# print lists
print "list1:    ", list1
print "listEven: ", listEven
print "listOdd:  ", listOdd
