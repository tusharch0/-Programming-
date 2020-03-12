# Python program to find number of bits
# necessary to represent an integer in binary

# input a number
num = int(input("Enter an integer number: "))

# total bits to represent number
bits = num.bit_length()

print("bits required to store ", num, " = ", bits)
print("binary value of ", num, " is = ", bin(num))
