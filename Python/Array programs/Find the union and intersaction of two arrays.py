a = list(map(int ,input ("Enter element of first list : ").split()))
b = list(map(int ,input ("Enter element of second list : ").split()))

A = list(set(a)|set(b))
B = list(set(a)&)set(b))

print('Union of the array :',A)
print("intersection of the array :",B)
