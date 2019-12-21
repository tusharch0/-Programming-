n= int (input ())
l= list (map(int ,input ().strip().split(" ")))
odd =[]
even =[]
for i in l:
    if (i%2!=0):
        odd.append (i)
    else :
        even.append(i)
print ("list of odd number is : ",odd)
print ("list of even number is : ",even )