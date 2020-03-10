# Given a positive integer number n, you have to write a program that generates a dictionary d which contains (i, i*i) such that i is the key and i*i is its value, where i is from 1 to n (both included).
# Then you have to just print this dictionary d.
#
# Example:
# Input: 4
#
# will give output as
# {1: 1, 2: 4, 3: 9, 4: 16}
#
# Input Format:
# Take the number n in a single line.
#
# Output Format:
# Print the dictionary d in a single line.
#
#
# Example:
#
# Input:
# 8
#
# Output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


n = int(input())

dict = {}
for i in range(1, n+1):
    dict[i] = i*i

print(dict)
