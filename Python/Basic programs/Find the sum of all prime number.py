N=1000
s=0
Primes = [True for k in range (N+1)]
p=2
Primes [0] = False 
Primes [1] = False 
while (p*p<=N):
    if Primes[p]==True:
        for j in range (p*p,N+1,p):
            Primes[j]=False
    p+=1
for i in range (2,N):
    if Primes[i]:
        s+=i
print('The sum of prime number : ')