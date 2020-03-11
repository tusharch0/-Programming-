# importing the module
from itertools import permutations

# input the sting
s = input('Enter a string: ')

A = []
b = []
p = permutations(s)

for k in list(p):
    A.append(list(k))
    for j in A:
        r = ''.join(str(l) for l in j)
        b.append(r)

print('Number of all permutations: ', len(b))
print('All permutations are: ')
print(b)
