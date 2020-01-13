i = int (input("Enter the first number :"))
j = int (input("Enter the second number :"))
k = int (input ("Enter the third number :"))
if (i>j):
    if (i>k):
        print(i," is greatest ")
    else:
        print(k," is greatest ")
else:   
    if (k>j):
        print (k," is greatest ")
    else :
        print(j," is greatest ")