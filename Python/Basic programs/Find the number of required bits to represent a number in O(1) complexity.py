from math import log2,floor 
def countBits(num):
    bits = floor(log2(num)+1)
    return bits

if __name__ =="__main__":
    Num =10
    print (countBits(Num))
    Num =32
    print (countBits(Num))