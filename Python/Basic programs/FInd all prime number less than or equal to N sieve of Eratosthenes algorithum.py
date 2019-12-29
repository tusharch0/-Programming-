N = int (input ("Input the value of n :"))
Primes = [True for  k in range (N+1) ]
p = 2
Print[1]=False
Prime[0]=False

while (p*p<=N):
    if Primes[p]==True:
        for j in range(p*p,N+1,p):
            Primes[j]=False
    p+=1
for i in range(2,N):
    if Primes[i]:
        print(i,end=' ')