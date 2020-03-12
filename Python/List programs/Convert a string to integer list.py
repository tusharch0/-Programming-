print (int('0'))
print (int('1'))
print (int('2'))
print (int('3'))
print (int('4'))
print (int('5'))
print (int('6'))
print (int('7'))
print (int('8'))
print (int('9'))

#OR
# program to convert string to integer list
# language: python3

# declare a list
str1 = "12345"

# list variable to integeres
int_list = []

# converting characters to integers
for ch in str1:
    int_list.append(int(ch))

# printing the str_list and int_list
print("str1: ", str1)
print("int_list: ", int_list)

#OR
# program to convert string to integer list
# language: python3

# declare a list
str1 = "12345ABCD"

# list variable to integeres
int_list = []

# converting characters to integers
for ch in str1:
    int_list.append(int(ch))

# printing the str_list and int_list
print("str1: ", str1)
print("int_list: ", int_list)
