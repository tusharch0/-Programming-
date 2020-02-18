# program to retrieve string in reverse as well as in normal form
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

s = "Hello_world"

print("The original string  is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))
print()

# program to demonstrate the use of membership operator(in,not in)
str1 = "Hello world"
list1 = [10, 20, 30, 40, 50]

if 'w' in str1:
	print ("Yes! w found in ", str1)
else:
	print ("No! w does not  found in " , str1)

if 'X' not in str1:
	print ("yes! X does not exist in ", str1)
else:
	print ("No!  X exists in ", str1)

if 30 in list1:
	print ("Yes! 30 found in ", list1)
else:
	print ("No! 30 does not found in ", list1)

if 90 not in list1:
	print ("Yes! 90 does not exist in ", list1)
else:
	print ("No! 90 exists in ", list1)
print()

# program to demonstrate the use of slice notation
str1 = "Hello"
str2 = "_world"
print(str1)
print(str1[0])
print(str1[0], str1[1])
print(str1[2:5])  # printing element 2nd to 5th
print(str1[1:])  # printing 1 to all
print(str2 * 2)  # string 2 two times
print()

# program to demonstrate string concatenate (abc+ pqr)
print(str1 + str2)

# program to demonstrate the use of replication of alphabet
print(str1*4)

# program to demonstrate relation operator
print("abc">"aaa")
print("abc">="aaa")
print("abc"<="aaa")
print("abc"<"aaa")
print("abc"=="aaa")
print("abc"!="aaa")

# program to demonstrate various string function

#1. capitalize()
x='abc'.capitalize()   
print(x)

#2. count()
msg = "  hello, weLcoMe Tushar choUdhary  "
sub1="welcome"
sub2= "tushar"
sub3= "choudhary"
x= msg.count("tushar")  
print(x)

#3. endswidth()
x= msg.endswith("tushar")  
print(x)
x= msg.endswith("choudhary")
print(x)

#4. casefold()
x= msg.casefold()
print(x)

#5. index(string)
x= msg.index("weLcoMe")
print(x)

#6. isalnum()
x= msg.isalnum()
print(x)

#7. isalpha
x= msg.isalpha()
print(x)

#8. isdigit
x= msg.isdigit()
print(x)

#9. islower
x= msg.islower()
print(x)

#10. isupper
x= msg.isupper()
print(x)

#11. isspace()
x = msg.isspace()
print(x)

#12. len(str)
x = len(msg)
print(x)

#13. lower()
x= msg.lower()
print(x)

#14. upper()
x= msg.upper()

#15. startswith(string)
x= msg.startswith("hello")
print(x)

#16. swapcase()
x= msg.swapcase()
print(x)

#17. lstrip()
x= msg.lstrip()
print(x)

#18. rstrip()
x= msg.rstrip()
print(x)

#19. center()
#20. encode()
#21. expandtabs()
#22. find()
#23. format() 
#24. format_map()
#25. isdecimal()
#26. isidentifier()
#27. isnumeric()
#28. isprintable()
#29. istitle()
#30. join
#31.!just
#32. maketrans()
#33. partition()
#34. replace()
#35. rfind()
#36. rindex()
#37. rjust()
#38. rpartition()
#39. rstrip()
#40. split()
#41. splitlines()
#42. strip()
#43. title()
#44. translate()
#45. zfill()
