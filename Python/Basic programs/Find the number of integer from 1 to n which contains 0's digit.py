n= int (input ('Enter the value of n: '))
c=0
z=str(0)
for j in range(1,n+1):
    if z in str(j):
        c+=1
print('{} number has zero as digits up to {}'.format(c,n))