P = int (input ('Enter a number: '))
s=int (bin(P)[2:])
r=str (s)[::-1]
if int (r)==s:
    print("The binary representation of the number is a palindrome .")
else :
    print ("The binary representation of the number is not a palindrome .")