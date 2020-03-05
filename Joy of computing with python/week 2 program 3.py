#Given two numbers(integers) as input, print the smaller number.

#Input Format:
#The first line of input contains two numbers separated by a space

#Output Format:
#Print the smaller number

#Example:

#Input:
#2 3

#Output:
#2

x, y = input().split(" ")
x = int(x)
y = int(y)

if(x < y):
    print(x)
else:
    print(y)

#Or 

a, b = input().split()
if a < b:
  print(a)
else:
  print(b)

#Or

x, y = map(int, input().split())
print(x if x > y else y)
