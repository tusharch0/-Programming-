# function to calculate and return the sum
# parameters:
# a, b - integral numbers in string format
# return: sum of the numbers in integer format


def calculateSum(a, b):
	s = int(a) + int(b)
	return s


# Main code
# take two integral numbers as strings
num1 = "10"
num2 = "20"

# calculate sum
sum = calculateSum(num1, num2)

# print sum
print ("Sum = ", sum)
