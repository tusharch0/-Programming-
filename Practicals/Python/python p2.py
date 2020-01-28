# program to demonstrate the use of if, if-else, while ,for ,break and continue

# if statement 
i= int (input("Enter any number :"))
if(i>0):
    print("Positive number ")

# if-else statement 
if (i%2==0):
    print("Even number ")
else:
    print("Odd number ")
print()

# nested if-else
a= int (input("Enter the first number :"))
b= int (input("Enter the second number :"))
c= int (input("Enter the third number :"))

if (a>b and a>c):
    print("A is greatest ")
elif (b>a and b>c):
    print("B is greatest ")
elif (c>a and c>b):
    print("C is greatest ")

# print the table of the number enter by the user 
a=int (input ("Enter the number "))
for i in range (1,11,1):
    print(a,"*",i," = ",a*i)

# sum of natural number from 1 to 10
sum=0
for i in range (1,11,1):
    sum = sum +i
    print("Addition of ",i,"number is ",sum)
    
# While loop
a=0
while a<5:
    print(a)
    a=a+1
print()

# for loop
for i in range (5):
    print (i)
print()
for i in range (5,8):
    print (i)
print()
for i in range (2,9,2):
    print(i)
print()
for i in range (9,2,-2):
    print(i)
print()

# Break statement 
fruits =["apple ","banana","guava","oranges"]
for i in fruits :
    if i=="guava":
        break
    print (i)
print()

# Continue statement
for i in fruits:
    if i =="guava":
        continue
    print(i)