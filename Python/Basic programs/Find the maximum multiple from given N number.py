n =0
num =0
maxnum =0
x= int (input("Enter the num of which you want to find the highest multiple: "))
while n<5:
    num = int (input("Enter your number :"))
    if num%x ==0:
        if num>maxnum:
            maxnum =num 
        else :
            print("Not multiple ")

        n +=1
print("The maximum multiple :",maxnum)