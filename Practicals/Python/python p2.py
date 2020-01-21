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
fruits =["apple ","banana","guava","grapes","oranges"]
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