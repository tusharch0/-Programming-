# Python program to generate and print
# dictionary of numbers and square (i, i*i)

# declare and assign n
n = 10

# declare dictionary
numbers = {}

# run loop from 1 to n
for i in range(1, n+1):
	numbers[i] = i * i

# print dictionary
print (numbers)
