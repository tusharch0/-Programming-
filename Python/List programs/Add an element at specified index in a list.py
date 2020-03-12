# Declaring a list
list = [10, 20, 30]

# printing elements
print(list)
# O/P will be: [10, 20, 30]

# inserting "ABC" at 1st index
list.insert(1, "ABC")
# printing
print(list)
# O/P will be: [10, 'ABC', 20, 30]

# inserting "PQR" at 3rd index
list.insert(3, "PQR")
# printing
print(list)
# O/P will be: [10, 'ABC', 20, 'PQR', 30]

# inserting 'XYZ' at 5th index
list.insert(5, "XYZ")
print(list)
# O/P will be: [10, 'ABC', 20, 'PQR', 30, 'XYZ']

# inserting 99 at second last index
list.insert(len(list) - 1, 99)
# printing
print(list)
# O/P will be: [10, 'ABC', 20, 'PQR', 30, 99, 'XYZ']
