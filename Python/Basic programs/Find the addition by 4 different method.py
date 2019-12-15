# Method 1 
if __name__ == "__main__" :
    a= int (input())
    b= int (input())
    sum_num = a+b
    print("sum of two number is : ",sum_num)

# Method 2 
def sum_num(a,b) :
    return a+b

if __name__ == "__main__" :
    a = int(input())
    b = int(input())

    print ("Sum of the number : ",sum_num(a,b))

# Method 3
if __name__ =="__main__" :
    a,b = input().split()
    rslt = int (a) + int (b)
    print("sum of two number is : ",rslt)

# Method 4
if __name__ =="__main__" :
    a = list(map(int ,input().split()))
    print ("sum of two number is :",sum(a)) 