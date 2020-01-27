# factorial of a given number 
#using recursion 
fac =1
def fact (a):
    if a==1 :
        fac=1
    else :
        fac = a*fact(a-1) 
    return fac 

i= int (input ("Enter the number :"))
print(fact (i))

#using loop method 1 (iteration )
a= int (input("Enter the number :")) 
result =1
for i in range (a,0,-1):
    result =result *i
print(result)

#using loop method 2
a= int (input("Enter the number :"))
res=1
for i in range (1,a+1,1): 
    res=res*i
print(res)