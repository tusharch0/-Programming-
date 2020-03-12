# N largest and smallest element in a list
# by function and by the help of heapq module

#function to find n largest element
import heapq


def largest_ele(l, n):
    s = []
    for i in range(n):
        s.append(max(l))  # append max of list in a new list
        l.remove(max(l))  # remove max of list from the list
    print('by largest_ele function: ', s)

#function to find n largest element


def smallest_ele(m, n):
    t = []
    for i in range(n):
        t.append(min(m))  # append min of list in a new list
        m.remove(min(m))  # remove min of list from the list
    print('by smallest_ele function: ', t)


l = [2, 4, 6, 8, 10]
m = [0, 1, 2, 3, 4, 5, 6]
n = 2
largest_ele(l, n)
smallest_ele(m, n)

# using the inbuilt module function
# heapq.nlargest and heapq.nsmallest
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print('BY heapq.nlargest: ', heapq.nlargest(3, nums))  # Prints [42, 37, 23]
print('BY heapq.nsmallest: ', heapq.nsmallest(3, nums))  # Prints [-4, 1, 2]
