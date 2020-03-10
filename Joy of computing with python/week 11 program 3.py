#Write a Python program to push all zeros to the end of a given list a. The order of the elements should not change.

#Input Format:
#Elements of the list a with each element separated by a space.

#Output Format:
#Elements of the modified list with each element separated by a space. After the last element, there should not be any space.

#Example:

#Input:
#0 2 3 4 6 7 10

#Output:
#2 3 4 6 7 10 0


s = list(input().split())
r = []
z = 0
for i in s:
    if(i == '0'):
        z += 1
        continue
    r.append(i)
r = r + ['0'] * z
print(' '.join(r), end='')


def move_zero(num_list):
    a = [0 for i in range(num_list.count(0))]
    x = [i for i in num_list if i != 0]
    x.extend(a)
    return(x)


num_list = list(map(int, input().split()))

res = move_zero(num_list)

for i in range(len(res)):
    if(i == len(res)-1):
        print(res[i], end="")
    else:
        print(res[i], end=" ")
