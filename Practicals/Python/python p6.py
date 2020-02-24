# Using recursive and non recursive function, write a program to find the factorial of a given number 

#using recursion function
fac = 1
def fact(a):
    if a == 1:
        fac = 1
    else:
        fac = a*fact(a-1)
    return fac


i = int(input("Enter the number :"))
print(fact(i))

#Non recursive method 1 
a = int(input("Enter the number :"))
result = 1
for i in range(a, 0, -1):
    result = result * i
print(result)

#Non recursive method 2
a = int(input("Enter the number :"))
res = 1
for i in range(1, a+1, 1):
    res = res*i
print(res)

# The finance department of a company wants to compute the monthly pay of its employees. Display all the employee details Also calculate the total yearly income tax of employee based on the prevailing income tax slabs Monthly pay should be calculated as mentioned in the formula below.
# Monthly Pay = Number of hours worked in a week * pay rate per hour * no. of week in a month
# a) The number of hours worked by the employee in a week should be considered as 40
# b) Pay rate per hour should be considered as Rs 400
# C) Number of weeks in a month should be considered as 4 
# Write a Python program to implement the above real world.

emp = input("Enter the name of employee : ")
hrs = int(input("Enter the no of hours he worked :"))
payRate = int(input("Enter the pay rate :"))
week = int(input("Enter the niumber of weeks :"))
sal = 0
sal = hrs*payRate*week
yearSal = 0
yearSal = sal*12
tax = 0
print("Monthly Salary of Employee is : ", sal)
if (yearSal <= 250000):
    tax = 0
elif (yearSal <= 500000 and yearSal >=250000):
    tax = (yearSal-250000)*0.05
elif (yearSal >= 500000 and yearSal <= 1000000):
    tax = 12500+(yearSal - 500000)*0.2
else:
    tax = 12500+100000+(yearSal-1000000)*0.3

print("Tax is : ", tax)
