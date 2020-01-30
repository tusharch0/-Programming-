num = int (input("Enter the number :"))
temp = num
res = 0
while (temp != 0):
    rem = temp % 10
    res += rem**3
    temp //= 10
if (num == res):
    print(num, "is armstrong ")
else:
    print(num, "is not armstrong")
