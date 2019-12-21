def factorial (num):
    if num <0:
        print ("Invalid number ...")
    elif num==0 or num==1:
        return 1
    else :
        return num* factorial (num-1 )

if __name__=='__main__':
    x= int (input ("Enter an integer number :"))
    print ("Factorial of ",x, " is = ",factorial(x))
    x= int (input ("Enter another integer number :"))
    print ("Factorial of ",x, " is = ",factorial(x))
    x= int (input ("Enter another integer number :"))
    print ("Factorial of ",x, " is = ",factorial(x))