# define a list
list = [10, 20, 30, 40, 50, 60]

# Create list1 with half elements (first 3 elements)
list1 = list[:3]
# Create list2 with next half elements (next 3 elements)
list2 = list[3:]

# print list (s)
print "list : ", list
print "list1: ", list1
print "list2: ", list2

#OR
# define a list
list = [10, 20, 30, 40, 50, 60]

# Create list1 with half elements (first 3 elements)
list1 = list[0:3]
# Create list2 with next half elements (next 3 elements)
list2 = list[3:6]

# print list (s)
print "list : ", list
print "list1: ", list1
print "list2: ", list2

#OR
# define a list
list = [10, 20, 30, 40, 50, 60]

# get the length of the list
n = len(list)

# condition to check length is EVEN or not
# if lenght is ODD, show message and exit
if(n % 2 != 0):
    print "List has ODD number of elements."
    exit()

# Create list1 with half elements (first 3 elements)
list1 = list[0:n/2]
# Create list2 with next half elements (next 3 elements)
list2 = list[n/2:n]

# print list (s)
print "list : ", list
print "list1: ", list1
print "list2: ", list2
