# Function in python 
def sum(a,b):             # a,b are the perameters to sum function 
    result =a+b
    return result         # return statement 

i=int(input ("Enter the first number :"))
j=int(input("Enter the second number :"))
print(sum (i,j))          # passing of argument in function

print(sum(2,4))           # 2,4 are arguments 
print(sum(b=2,a=3))       # keyword argument 

b=20                      # globle variable 
def sum2(a,msg="Hello"):  # default perameters
    b=10                  # local variable 
    print(a,msg)

print(sum2(4,'John'))
print(sum2(5))
print(b)