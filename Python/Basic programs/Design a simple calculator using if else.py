print ("Calculate ")
print("1. Add")
print("2. Substraction")
print("3. Multiply")
print("4. Divide ")

ch=int(input ("Enter Choice(1-4) :"))
if ch==1:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a+b
    print("Sum= ",c)
elif ch==2:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a-b
    print("Differece =",c)
elif ch==3:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a*b
    print("product =",c)
elif ch==4:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b
    print ("Quotient =",c)
else :
    print("Invalid Choice ")