def count_substring (string ):
    substring =0
    n= len(string)
    substring = n*(n+1)//2
    return substring 

def general_method (string):
    substring =0
    n = len(string)
    substr =[]
    for i in range (n):
        for j in range (i,n):
            substr.append(string [i:j])
    substring = len(substr)

    return substring

if __name__ =='__main__':
    string = 'Hello_world'
    print("The total number of substring = %d"% count_substring(string))
    print("The total number of substring = %d"% general_method(string))
