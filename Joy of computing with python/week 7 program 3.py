# Given a matrix with N rows and M columns, the task is to check if the matrix is a Binary Matrix. A binary matrix is a matrix in which all the elements are either 0 or 1.
#
# Input Format:
# The first line of the input contains two integer number N and M which represents the number of rows and the number of columns respectively, separated by a space.
# From the second line, take N lines input with each line containing M integer elements with each element separated by a space.
#
# Output Format:
# Print 'YES' or 'NO' accordingly
#
# Example:
#
# Input:
# 3 3
# 1 0 0
# 0 0 1
# 1 1 0
#
# Output:
# YES
#


n, m = (input().split(" "))
n = int(n)
m = int(m)
a = []
z = []
for i in range(n):
    l = []
    for j in range(m):
        l.append(0)
    a.append(l)

for i in range(n):
    o = [int(g) for g in input().split(" ")]
    for j in range(m):
        a[i][j] = o[j]
        z.append(a[i][j])

for i in z:
  if i > 1:
    print("NO", end='')
    break
else:
  print("YES", end='')


def isBinaryMatrix(mat, M, N):
    for i in range(M):
        for j in range(N):
            # Returns false if element
            # is other than 0 or 1.
            if ((mat[i][j] == 0 or mat[i][j] == 1) == False):
                return False

    # Returns true if all the
    # elements are either 0 or 1.
    return True


a, b = map(int, input().split())


m = []
for i in range(1, a+1):
    l = list(map(int, input().split()))
    m.append(l)
if (isBinaryMatrix(m, a, b)):
    print("YES")
else:
    print("NO")
