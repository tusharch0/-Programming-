def binToDec(bin_value):
    decimal_value =0
    count =0
    while (bin_value != 0):
        digit = bin_value % 10
        decimal_value =decimal_value +digit * pow (2,count )
        bin_value  =bin_value//10
        count +=1
        return decimal_value

if __name__ =='__main__':
    binary = int (input("Enter a binary value :"))
    print ("Decimal of binary",binary," is :",binToDec(binary))
    
    binary = int (input("Enter another binary value :"))
    print ("Decimal of binary",binary," is :",binToDec(binary))
    
    binary = int (input("Enter another binary value :"))
    print ("Decimal of binary",binary," is :",binToDec(binary))