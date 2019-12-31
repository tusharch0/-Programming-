# find the GCD of two non-zero number
import math
m,n =map (int (input ('Enter the non zero number :').split()))
g=map.gcd(m,n)
print('GCD of {} and {} '.format (m,n,g))

# find the GCD of the array
import math
A = [40,15,25,50,70,10,95]
b= A[0]
for j in range (1,len(A)):
    s=math.gcd(b,A[j])
    b=s
print('GCD of array element is {}'.format(b))