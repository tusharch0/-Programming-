# Write a program to count the numbers of characters in the string and store them in a dictionary data structure
str = "Hello World"
str1 = {}
for i in str:
    if i in str1:
        str1[i] += 1
    else:
        str1[i] = 1
print(str1)


# Write a program combine lists that combines these lists into a dictionary.
str = ["Tushar",'Abhi','Rahul']
str1 = ['Khan','Choudhary','Kumar']
names = zip(str,str1)
for a,b in names :
    print(a,b)