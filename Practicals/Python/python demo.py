def fun(i,f):
    print(i)
    if(i==0):
        f=1
        fun(i+1,f)
    if(i == 128):
        f = -1
        fun(i-1,f)
    if(i == 1):
        fun(i+1,f)
    if(i == -1):
        fun(i+1,f)
print(fun(9))