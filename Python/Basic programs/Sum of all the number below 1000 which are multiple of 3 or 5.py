n = 1000
s = 0
for k in range (1,n+1):
    if k%3==0 or k%5==0:
        s+=k
print('The sum of the number :',s)