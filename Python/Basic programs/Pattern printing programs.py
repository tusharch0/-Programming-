# *
# * *
# * * *
# * * * *
# * * * * *

for row in range (0,5) :
    for column in range (0,row+1):
        print ("*",end ="")

    print ('\r')

# 1
# 1 2
# 1 2 3
# 1 2 3 4 
# 1 2 3 4 5

for row in range (0,5):
    n=1
    for column in range (0,row+1 ):
        print (n,end=" ")
        n=n+1
        print('\r')

# 1
# 2  3 
# 4  5  6 
# 7  8  9  10
# 11 12 13 14 15

n=1 
for row in range (0,5) :
    for column in range (0,row +1) :
        print(n,end= "  ")
        n=n+1

    print('\r')

# A
# A B
# A B C
# A B C D
# A B C D E

for row in range (0,5) :
    n=65
    for column in range (0,row+1):
        c= chr(n)
        print(c, end=" ")
        n=n+1

    print('\r')
    
