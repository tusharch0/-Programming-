str = "Python is a programing language "
words= list (str.split(' '))
print("str : ",str)
print("List convert string :",words)
print("Even length words: ")
for W in words :
    if (len(W)%2==0):
        print(W)