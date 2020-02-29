str1 = "8789"
str2 = "Hello123"
str3 = "123Hello"
str4 = "123 456"


print("str1.isdigit(): ",str1.isdigit())
print("str2.isdigit(): ",str2.isdigit())
print("str3.isdigit(): ",str3.isdigit())
print("str4.isdigit(): ",str4.isdigit())
print()

if str1.isdigit():
    print("str1 contain a number ")
else :
    print("str1 does not contain number ")

if str2.isdigit():
    print("str2 contain a number ")
else:
    print("str2 does not contain number ")

if str3.isdigit():
    print("str3 contain a number ")
else:
    print("str3 does not contain number ")

if str4.isdigit():
    print("str4 contain a number ")
else:
    print("str4 does not contain number ")
