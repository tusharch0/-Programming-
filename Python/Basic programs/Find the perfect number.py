if __name__ == '__main__':
    i=2; 
    sum = 1
    n =int(input("Enter a number : "))
    while (i<=n//2):
        if (n%i==0):
            sum +=i
        i +=1

    if sum == n:
        print (n," is a perfect number ")
    else :
        print (n," is not a perfect number ")
