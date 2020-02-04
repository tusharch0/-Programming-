# user defined function to find the maximum, minimum, mean, mode, from a list of numbers 
list = []
len = int (input("Enter the no of element : "))
for i in range(len):
    num =int (input ("list[{0}]: ".format(i)))
    list.append(num)

z=list[0]
for i in list :
    if (i>z):
        z=i
print("Maximum is :",z)

y = list[0]
for i in list :
    if (i<y):
        y=i
print("Minimum is :",y)

sum =0
t=0
for i in list :
    sum= sum +i
    t=t+1
mean = sum/t
print("Mean is :",mean)

a=int(t/2)
median = list[a]
print("Median is :",median)

temp=[]
count =0
for i in list:
    for j in list :
        if(j==i):
            count =count+1
    temp.append(count)
    count =0

maximum =temp[0]
point = 0
pos =0
for i in temp:
    if (i>maximum):
        maximum=i
        pos=point
    point=point+1

print("Mode is :",list[pos])                                                     