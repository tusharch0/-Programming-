def array_abc (char):
    for i in range (len(char)-2):
        if char [i]== 'a' and char[i+1] == 'b' and char [i+2]== 'c':
            return True 
        return False

print(array_abc(['a','x','a','b','c']))