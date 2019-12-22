from time import time 
from math import sqrt
def general_approch(n):
    start = time()
    count= 0
    for i in range (2,n):
        flag =0
        x= i//2+1
        for j in range (2,x):
            if i%j==0:
                flag =1 
                break
        if flag ==0:
            count +=1
    stop =time ()
    print("Count = ",count,"Elapsed time: ",stop - start,"second ")

def count_primes_by_sqrt_method(n):
    start =time()
    count =0
    for val in range (2,n):
        root = round(sqrt (val))+1
        for trial_factor in range (2,root ):
            if val % trial_factor ==0 :
                break
        else: 
            count +=1
    stop = time() 
    print ("count =",count ,"Elapsed time :",stop-start, "second ")

def seive (n):
    start = time ()
    nonprimes =n * [False] 
    count =0
    nonprimes[0] = nonprimes [1] = True 
    for i in range (2,n):
        if not nonprimes[i]:
            count +=1 
            for j in range (2*i,n,i):
                nonprimes[j] = True
    stop = time ()
    print ("count =",count,"Elapsed time :",stop -start,"seconds ")

def main():
    print ("For N== 200000\n")
    print ('Sieve of Eratosthenes Method ')
    seive (200000)
    print ('\nSquare root Method ')
    count_primes_by_sqrt_method (200000)
    print('\nGeneral Approach ')
    general_approch(200000)

main()        