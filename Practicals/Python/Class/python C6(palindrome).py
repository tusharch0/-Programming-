# for integer 
n =int (input("Enter the number: "))
t=n
b=0
while (n>0):
    a=n%10
    b=b*10+a
    n=n//10
if (b==t):
    print("Palindrome ")
else :
    print ("Not palindrome")

# for string 
num = input("Enter the string : ")
num2=''
for i in num:
    num2= i+num2
if (num2==num):
    print("Palindrome")
else:
    print("Not palindrome ") 