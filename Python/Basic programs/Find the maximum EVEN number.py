n =0 
num =0
maxnum =0

while n<10:
    num = int (input("Enter your  number : "))
    if num%2==0:
        if num> maxnum:
            maxnum=num
    n+=1
print ("The maximum Even number :",maxnum)