# Given a number n, you have to print the factorial of this number. To know about factorial please click on this link.
#
# Input Format:
#
# A number n.
#
# Output Format:
#
# Print the factorial of n.
#
# Example:
#
# Input:
# 4
#
# Output:
# 24


n = int(input())
fact = 1

for i in range(1, n+1):
    fact = fact * i

print(fact)


# or


k = int(input())

fac = 1
for i in range(1, k+1):
    if(k == 0):
        break
    fac = fac*i

print(fac)
