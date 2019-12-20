num = int(input ("Enter a number with multiple digits : "))
n=0
while num>0:
    a=num%10
    num =num -a
    num=num/10
    print(int (a),end="")
    n=n+1
print(n)