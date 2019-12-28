
import math 
A,B,C = map(int,input ().split ())
d=((B**2)-4*A*C)
if  d>=0:
    s= (-B+(d)**0.5)/(2*A)
    p= (-B-(d)**0.5)/(2*A)
    print(math.floor(s),math.floor(p))
else:
    print('The roots are imaginary')