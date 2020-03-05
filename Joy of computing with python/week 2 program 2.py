#In this assignment, you will have to take two numbers(integers) as input and print the addition.
#Input Format:
#The first line of the input contains two numbers separated by a space.

#Output Format:

#Print the addition in single line

#Example:

#Input:
#4 2

#Output:
#6

x, y = input().split(" ")
x = int(x)
y = int(y)

print(x+y)

#or

a, b = input().split()
c = 0
c = int(a)+int(b)
print(c)

#or

x, y = map(int, input().split())
print(x+y)