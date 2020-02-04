# nested if else
a= int (input("Enter the first number :"))
b= int (input("Enter the second number :"))
c= int (input("Enter the third number :"))

if (a>b and a>c):
    print("A is greatest ")
elif (b>a and b>c):
    print("B is greatest ")
elif (c>a and c>b):
    print("C is greatest ")