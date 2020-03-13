# Declaring a list
list = [10, 20, 30, 40, 30]

# print list
print "List element:"
for l in range(len(list)):
	print(list[l])

# removing 30 from the list
list.remove(30)

# print list after removing 30
print "List element after removing 30:"
for l in range(len(list)):
	print(list[l])
