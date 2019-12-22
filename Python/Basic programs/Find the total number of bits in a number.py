num = 61 
print ("binary value of {0} id {1}".format (num,bin(num)))
length =len(bin(num))
length -=2
print ("total number of bits :",length)

# by defining function
def totalBits (n):
    return len(bin(n)[2: ])

a = 61
b = 12 
print ("Total bits in {0} = {1}".format (a,totalBits (a)))
print ("Total bits in {0} = {1}".format (b,totalBits (b)))