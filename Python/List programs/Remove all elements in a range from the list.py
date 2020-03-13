# Declaring a list
list = [10, 20, 30, 40, 50]

# print list
print "List element:"
for l in range(len(list)):
	print(list[l])

# delete element from index 1 to 30del list[1.3]
del list[1:3]

# print list after deleting
# element from index 1 to 3
print "List element after del[1:3]:"
for l in range(len(list)):
	print(list[l])
