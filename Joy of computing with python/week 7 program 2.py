# Given a square matrix of N rows and columns, find out whether it is symmetric or not.
#
# Input Format:
# The first line of the input contains an integer number n which represents the number of rows and the number of columns.
# From the second line, take n lines input with each line containing n integer elements with each element separated by a space.
#
# Output Format:
# Print 'YES' if it is symmetric otherwise 'NO'
#
# Example:
#
# Input:
# 2
# 1 2
# 2 1
#
# Output:
# YES


n = int(input())
a = []
z = []
for i in range(n):
    l = []
    l2 = []
    for j in range(n):
        l.append(0)
        l2.append(0)
    a.append(l)
    z.append(l2)

for i in range(n):
    o = [int(g) for g in input().split(" ")]
    for j in range(n):
        a[i][j] = o[j]
for i in range(n):
    for j in range(n):
        z[i][j] = a[j][i]
if (z == a):
    print("YES", end='')
else:
    print("NO", end='')


# or


def isSymmetric(mat, N):
    for i in range(N):
        for j in range(N):
            if (mat[i][j] != mat[j][i]):
                return False
    return True


a = int(input())


m = []
for i in range(1, a+1):
    l = list(map(int, input().split()))
    m.append(l)
if (isSymmetric(m, a)):
    print("YES")
else:
    print("NO")
