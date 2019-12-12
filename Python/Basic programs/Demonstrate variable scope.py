a=100
def func():
    b=200
    print("a: ",a,"b: ",b)

if __name__=='__main__':
    c=200
    print ("a: ",a)
   #print ("b: ",b) // local variable will give error
    print ("c: ",c)

    func()
    a=a+10
    print ("a: ",a)