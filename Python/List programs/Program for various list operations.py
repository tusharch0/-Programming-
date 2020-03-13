# Python code for various list operation

# declaring a list of integers
iList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# List slicing operations
# printing the complete list
print('iList: ', iList)
# printing first element
print('first element: ', iList[0])
# printing fourth element
print('fourth element: ', iList[3])
# printing list elements from 0th index to 4th index
print('iList elements from 0 to 4 index:', iList[0: 5])
# printing list -7th or 3rd element from the list
print('3rd or -7th element:', iList[-7])


# appending an element to the list
iList.append(111)
print('iList after append():', iList)

# finding index of a specified element
print('index of \'80\': ', iList.index(80))

# sorting the elements of iLIst
iList.sort()
print('after sorting: ', iList)

# popping an element
print('Popped elements is: ', iList.pop())
print('after pop(): ', iList)

# removing specified element
iList.remove(80)
print('after removing \'80\': ', iList)

# inserting an element at specified index
# inserting 100 at 2nd index
iList.insert(2, 100)
print('after insert: ', iList)

# counting occurances of a specified element
print('number of occurences of \'100\': ', iList.count(100))

# extending elements i.e. inserting a list to the list
iList.extend([11, 22, 33])
print('after extending:', iList)

#reversing the list
iList.reverse()
print('after reversing:', iList)
