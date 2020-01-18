# Sum of all the digit in the number given by user 
a=int (input("Enter the number "))
sum =0
while (a>0):
    b=int(a%10)
    a=int(a/10)
    sum = sum + b
print("Sum of digits is : ",sum)

