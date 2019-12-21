n= int (input ())
l=list (map(int ,input ().strip().split(' ')))
print ("Palindrome number are : ")
for i in l:
    num=str (i)
    if ("".join(reversed (num))==num):
        print(i)