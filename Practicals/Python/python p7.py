# Write a Python Program to find the maximum, minimum mean, median and mode from a list of numbers using user defined functions.

list = []
len = int(input("Enter the no of element : "))
for i in range(len):
    num = int(input("list[{0}]: ".format(i)))
    list.append(num)

z = list[0]
for i in list:
    if (i > z):
        z = i
print("Maximum is :", z)

y = list[0]
for i in list:
    if (i < y):
        y = i
print("Minimum is :", y)

sum = 0
t = 0
for i in list:
    sum = sum + i
    t = t+1
mean = sum/t
print("Mean is :", mean)

a = int(t/2)
median = list[a]
print("Median is :", median)

temp = []
count = 0
for i in list:
    for j in list:
        if(j == i):
            count = count+1
    temp.append(count)
    count = 0

maximum = temp[0]
point = 0
pos = 0
for i in temp:
    if (i > maximum):
        maximum = i
        pos = point
    point = point+1

print("Mode is :", list[pos])

# Write a Python program to multiply Matrices.

R1 = int(input("Enter the no. of row for matrix1 :"))
C1 = int(input("Enter the no. of column for matrix1 :"))
matrix1 = []
print("Enter the matrix1 rowwise ")
for i in range(R1):
    a = []
    for j in range(C1):
        a.append(int(input()))
    matrix1.append(a)

matrix2 = []
R2 = int(input("Enter the no. of row for matrix2 :"))
C2 = int(input("Enter the no. of column for matrix2 :"))
print("Enter the matrix2 rowwise ")
for i in range(R2):
    a = []
    for j in range(C2):
        a.append(int(input()))
    matrix2.append(a)

res = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
if (R2 == C1):
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                res[i][j] += matrix1[i][k]*matrix2[k][j]

    print("Resulting matrix is :")
    for i in range(3):
        for j in range(3):
            print(res[i][j], end=" ")
        print()

else:
    print("Matrix multiplication Not possible ")

