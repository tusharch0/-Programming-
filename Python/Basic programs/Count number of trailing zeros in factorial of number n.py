def find_trailing_zeros(num):
    sum =0
    i=1
    while (True):
        quotient =num//(5**i)
        if (quotient ==0):
            break
        sum += quotient
        i +=1
    return(sum)

if __name__ =="__main__":
    num =10
    print("Number of trailing zeros in factorial of ",num,"is :",find_trailing_zeros)
    num =20
    print ("Number of trailing zeroes in factorial of ",num,"is :",find_trailing_zeros)