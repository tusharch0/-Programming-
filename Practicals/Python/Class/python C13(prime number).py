count=0
a = int(input ("Enter the limit : "))
for i in range (2,a,1):
    for j in range (2,i,1):
        if (i%j==0):
            count =count+1

    if (count==0):
        print(i)
    count=0