a,b,p,q =map(int (input ('Enter the coordinate of the point : ').split()))
m= (q-b)/(p-a)
y=b
x=a
c=y-(m*x)
y=0
x=(y-c)/m
print('x-intercept of the line :',x)
x=0
y=(m*x)+c
print('y- intercept of the line ',y)