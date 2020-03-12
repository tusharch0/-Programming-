# taking input from the user
n = int(input('Enter the number: '))

# checking whether it is EVEN or ODD
if n % 2 == 0:
    print('{} is an even number.'.format(n))
else:
    print('{} is an odd number.'.format(n))

#OR
# input the list
A = list(map(int, input('Enter elements of List: ').split()))

# create two empty lists to store EVEN and ODD elements
B = []
c = []

for j in A:
    if j % 2 == 0:
        B.append(j)
    else:
        c.append(j)

print('List of even number: ', B)
print('List of odd number: ', c)
