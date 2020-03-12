# declare lists
numbers = []
squares = []
cubes = []

# start and end numbers
start = 1
end = 10

# run a loop from start to end+1
for count in range(start, end+1):
    numbers.append(count)
    squares.append(count**2)
    cubes.append(count**3)

# print the lists
print "numbers: ", numbers
print "squares: ", squares
print "cubes  : ", cubes


#or
# define function to add numbers in list
def listNumbers(a, b):
	#define dynamic list
	list = []
	for count in range(a, b+1):
	list.append(count)
	#return list
	return list

# define function to add squares in list


def listSquares(a, b):
	#define dynamic list
	list = []
	for count in range(a, b+1):
	list.append(count**2)
	#return list
	return list

# define function to add cubes in list


def listCubes(a, b):
	#define dynamic list
	list = []
	for count in range(a, b+1):
	list.append(count**3)
	#return list
	return list


# Main code
# declare lists
numbers = []
squares = []
cubes = []

# start and end numbers
start = 1
end = 10

# get values in lists
numbers = listNumbers(start, end)
squares = listSquares(start, end)
cubes = listCubes(start, end)

# print the lists
print "numbers: ", numbers
print "squares: ", squares
print "cubes  : ", cubes
