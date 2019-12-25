x = float (input("Enter the value of X : ") )
y = float (input ("Enter the value of Y : "))

temp = x
x=y
y = temp

print ("After swapping \nx= {0} and y= {1}".format(x,y))