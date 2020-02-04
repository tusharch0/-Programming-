# Function in python 
def sum(a,b):             # a,b are the perameters to sum function 
    result =a+b
    return result 

i=int(input ("Enter the first number :"))
j=int(input("Enter the second number :"))
print(sum (i,j))

print(sum(2,4))           # 2,4 are arguments 
print(sum(b=2,a=3))       # keyword arguments

def sum2(a,msg="Hello"):  # default perameter 
    print(a,msg)

print(sum2(4,'John'))
