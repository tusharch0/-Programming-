# Python program to print the binary value
# of the numbers from 1 to N

# input the value of N
n = int(input("Enter the value of N: "))

# printing the binary value from 1 to N
for i in range(1, n+1):
    print("Binary value of ", i, " is: ", bin(i))
