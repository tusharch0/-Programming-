def pow (x,y):
      if y==1:
        return x
      else:
        return pow (x,y-1)*x

if __name__=='__main__':
    x=2
    y=3
    result = pow(x,y)
    print(x," to the power ",y," is : ",result )
    x=10
    y=3
    result = pow(x,y)
    print(x," to the power ",y," is : ",result )
    x=12
    y=5
    result = pow(x,y)
    print(x," to the power ",y," is : ",result )
