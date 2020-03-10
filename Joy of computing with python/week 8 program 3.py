#Given a string S of lowercase letters, remove consecutive vowels from S. After removing, the order of the list should be maintained.

#Input Format:

#Sentence S in a single line

#Output Format:
#Print S after removing consecutive vowels

#Example:

#Input:
#your article is in queue

#Output:
#yor article is in qu


vowels = 'aeiou'
s = input()
i = 0
n = len(s)
while(i < n):
  print(s[i], end='')
  if(s[i] in vowels):
    while(i < n and s[i] in vowels):
      i += 1
    continue
  i += 1


def is_vow(c):

    # this compares vowel with
    # character 'c'
    return ((c == 'a') or (c == 'e') or
            (c == 'i') or (c == 'o') or
            (c == 'u'))

# function to print resultant string


def removeVowels(str):

    # print 1st character
    print(str[0], end="")

    # loop to check for each character
    for i in range(1, len(str)):

        # comparison of consecutive
        # characters
        if ((is_vow(str[i - 1]) != True) or
                (is_vow(str[i]) != True)):

            print(str[i], end="")


# Driver code
str = input()
removeVowels(str)
