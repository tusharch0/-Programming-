# uppercase and lowercase
print("Uppercase Alphabet are :") 
for i in range (65,91):
    print (chr(i),end =' ')
print("\nLowercase Alphabet are : ")
for j in range (97,123):
    print(chr(j),end=' ')

# convert character to numerical 
s= input ('\nEnter the character : ')
n= str(ord(s))
print('ASCII of character {} is {}'.format(s,n))

# convert numerical to character 
n= int (input('\nEnter the numerical value : '))
s= chr(n)
print('The character value of {} is {}'.format(s,str(n)))