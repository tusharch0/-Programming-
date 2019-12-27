def summ(x):
    if x==0:
        return 0
    if x==1:
        return 1
    if x==2:
        return 1
    if x==3:
        return 0
    else :
        return summ(x-1)+ summ(x-4)

if __name__ =='__main__':
    print("summ(0) :",summ(0))
    print("summ(1) :",summ(1))
    print("summ(2) :",summ(2))
    print("summ(3) :",summ(3))
    print("summ(10) :",summ(10))
    print("summ(14) :",summ(14))