def dynamic_fabonacci(n):
    l=[0]*(n+1)
    l[0] =0
    l[1] =1
    for i in range (2,n+1):
        l[i] =l[i-1]+l[i-2]
    return l

def fibonacci_by_formula (n):
    from math import sqrt 
    phi =(1+sqrt(5))/2
    fib =round (pow (phi,n)/sqrt(5))
    return fib

def main():
    n=8
    lst = dynamic_fabonacci(n)
    x= fibonacci_by_formula(n)
    print ('By Dynamic programming : ',lst [n])
    print ()
    print ('By formula : ',x)

main()