#Given a string S, check whether it contains any special character or not. Print 'YES' if it does else 'NO'.

#Input Format:

#The first line contains the string S

#Output Format:

#Print 'YES' or 'NO'

#Example:

#Input:
#Hi$my*name

#Output:
#YES


import re
ip = input()
l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
for i in range(65, 90):
  l.append(chr(i))
for i in range(97, 122):
  l.append(chr(i))
for i in ip:
  if i not in l:
    print("YES", end='')
    break
else:
  print("NO", end='')


# Function checks if the string
# contains any special character

def run(string):

    # Make own character set and pass
    # this as argument in compile method
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    # Pass the string in search
    # method of regex object.
    if(regex.search(string) == None):
        print("NO")

    else:
        print("YES")


S = input()

run(S)
