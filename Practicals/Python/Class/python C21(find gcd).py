def GCD(a,b):
    gcd =1
    if(a>b):
        min =b
    else :
        min =a
    min = min +1
    for i in range (2,min):
        if (a%i==0 and b%i==0):
            gcd = i

    return gcd

a= int (input ("Enter the first number: "))
b= int (input ("Enter the second number : "))
print(GCD(a,b))