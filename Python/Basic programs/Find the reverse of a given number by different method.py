if __name__ == "__main__":
    num =int (input ('Enter a number '))
    rev_num =0
    while (num):
        rem=num%10
        rev_num =rev_num* 10 +rem
        num//=10

    print('Reverse number is : ',rev_num)