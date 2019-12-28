n = 0
num = 0
minnum = 13
j=0
x= int (input ("Enter the num of which you want to find least multiple: "))
while n<5:
    num = int (input ("Enter your number :"))
    if num%x == 0:
        j =j +14
        if j==14:
            minnum = num
        if num<minnum :
            minnum = num 
    else :
        print ("Not multiple ")

    n +=1
if minnum%x == 0:
    print("The maximum multiple :",minnum)
else :
    print ("No multiple there")