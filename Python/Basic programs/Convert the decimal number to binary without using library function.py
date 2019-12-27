def decToBin(dec_value):
    bin_value = ''
    if dec_value >1:
        decToBin(dec_value//2)
    print(dec_value % 2 ,end = '')

if __name__== '__main__':
    decimal = int(input("Input a decimal number :"))
    print("Binary to decimal",decimal,"is ",end='' )
    decToBin(decimal)