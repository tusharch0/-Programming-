def reverseNum(num):
    rev_num =0
    while (num):
        rem =num%10
        rev_num =rev_num*10+rem
        num//=10
    return rev_num

if __name__ =="__main__":
    num=int (input ('Enter a number '))
    print('Reverse number is : ',reverseNum(num))