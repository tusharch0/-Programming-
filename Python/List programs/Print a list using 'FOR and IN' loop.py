# Declaring a list
list = [10, 20, 30, 40, 50]

# printing without using FOR and IN
print "List elements are: ", list
print " "  # prints new line

# printing using FOR and IN
print "List elements are: "

for L in list:
	print L

print " "  # prints new line

# calculating Sum of all elements
sum = 0
for L in list:
	sum += L
print "Sum is: ", sum
