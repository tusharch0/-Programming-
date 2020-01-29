a= int (input ("Enter the starting number : "))
b = int (input ("Enter the limit : "))
for i in range (a,b,1):
    if (i%7==0 and i%5==0):
        print(i)