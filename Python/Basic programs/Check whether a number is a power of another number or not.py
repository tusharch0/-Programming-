import math
a,b=map(int (input ('Enter two value ').split()))
s=math.log(a,b)
p=round(s)
if (b**p)==a:
    print('{} is the power of another number {}'.format (a,b))
else :
    print('{} is not the power of another number {}'.format (a,b))