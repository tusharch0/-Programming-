import math
A =[8,4,12, 40,26]
b= A[0]
m=1
for j in range (1,len(A)):
    s=math.gcd(b,A[j])
    b=s

for k in A:
    m=m*k
p=m//(b**(len(A)-1))

print("GCD of array element : ",b)
print("LCM of array element : ",p)