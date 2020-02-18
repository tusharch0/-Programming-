# write a program to find the largest of the three number input from the users

a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))
c = int(input("Enter the third number :"))

if (a > b and a > c):
    print("A is greatest ")
elif (b > a and b > c):
    print("B is greatest ")
elif (c > a and c > b):
    print("C is greatest ")

# write a program to find the gcd of three numbers.

def GCD(a, b):
    gcd = 1
    if(a > b):
        min = b
    else:
        min = a
    min = min + 1
    for i in range(2, min):
        if (a % i == 0 and b % i == 0):
            gcd = i

    return gcd

a = int(input("Enter the first number: "))
b = int(input("Enter the second number : "))
print(GCD(a, b))

# write a program to find first n prime number.

count = 0
a = int(input("Enter the limit : "))
for i in range(2, a, 1):
    for j in range(2, i, 1):
        if (i % j == 0):
            count = count+1

    if (count == 0):
        print(i)
    count = 0

# write a program to find the squre root of a number.

num = int (input("Enter the number :"))
sqrt = num**0.5
print("square root is :",sqrt)

# Using function, write a program to add natural number upto n where n is taken as a input from user 

n = int(input("Enter the limmit :"))
sum = 0
for i in range(1, n+1, 1):
    sum = sum+i

print("Sum of n natural number is :", sum)

# Using function, write a program to print fibonacci series till nth term (take input from user)

a = int(input("Enter the limit "))
i = 0
w = 0
x = 1
sum = 1
print(0)
while (i < a):
    print(sum)
    sum = w+x
    w = x
    x = sum
    i = i+1
