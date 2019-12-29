from datetime import datetime
import math
N =int (input("Enter the value of N"))
t_start = datetime.now ()
s = math.factorial(N)
print("factorial of the number : ",s)
t_end = datetime.now()
e=t_end-t_start
print("The execution time for factorial program : ",e)