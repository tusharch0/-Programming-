# define list
list = [10, 20, 30, 40, 50, 60]

start = 1
end = 4

if (start < 0):
    print "Invalid start index"
    quit()

if(end > len(list)-1):
    print "Invalid end index"
    quit()

# create another list
list1 = list[start:end+1]

# printth lists
print "list : ", list
print "list1: ", list1


#OR

# define list
list = [10, 20, 30, 40, 50, 60]

start = 1
end = 6

if (start < 0):
    print "Invalid start index"
    quit()

if(end > len(list)-1):
    print "Invalid end index"
    quit()

# create another list
list1 = list[start:end+1]

# printth lists
print "list : ", list
print "list1: ", list1
