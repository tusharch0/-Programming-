# input comma separated elements as string
str = str(raw_input("Enter comma separated integers: "))
print "Input string: ", str

# conver to the list
list = str.split(",")
print "list: ", list

# convert each element as integers
li = []
for i in list:
	li.append(int(i))

# print list as integers
print "list (li) : ", li
