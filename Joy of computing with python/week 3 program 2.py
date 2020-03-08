# Given two numbers as input, print the larger number.
#
# Input Format:
# The first line of input contains two numbers separated by a space
#
# Output Format:
# Print the larger number
#
# Example:
#
# Input:
# 2 3
#
# Output:
# 3
#
# Sample Test Cases Input	Output
# Test Case 1	2 3 3
# Test Case 2	3 4 4
# Test Case 3	4 5 5
# Test Case 4	10 8 10
# Test Case 5	100 10 100
# Test Case 6	0 1 1
# Test Case 7	10 9 10
# Test Case 8	9 6 9

x, y = map(int, input().split())
print(x if x > y else y)

# or

x, y = input().split(" ")
x = int(x)
y = int(y)

if(x > y):
    print(x)
else:
    print(y)
