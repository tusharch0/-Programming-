even =0
odd =0
number =[1,2,19,4,5,16,7,12,14]
for i in number:
    if (i%2==0):
        if (i>even):
            even=i
    elif (i%2!=0):
        if (i>odd):
            odd=i
print("Largest even number is ",even)
print("Largest odd number is ",odd)