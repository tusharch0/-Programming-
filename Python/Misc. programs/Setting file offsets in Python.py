# creating a file
f = open('file1.txt', 'w')

# writing content to the file
# first line
f.write('This is line1.\n')
# second line
f.write('This is line2.\n')
#third line
f.write('This is line3.\n')

# closing the file
f.close()

# now, reading operations ....
# openingthe file
f = open('file1.txt', 'r')
# reading 10 characters
str = f.read(10)
print('str: ', str)

# Check current offset/position
offset = f.tell()
print('Current file offset: ', offset)

# Reposition pointer at the beginning once again
offset = f.seek(0, 0)
# reading again 10 characters
str = f.read(10)
print('Again the str: ', str)

# closing the file
f.close()
