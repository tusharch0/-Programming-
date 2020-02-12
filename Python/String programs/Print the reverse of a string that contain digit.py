def reverse(n):
    s =str(n)
    p=s[::-1]
    return p

num = int(input("Enter a positive value :"))
print("The reverse integer : ",reverse(num))