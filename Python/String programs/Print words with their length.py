def splitString (str ):
    str =str.split(' ')
    for words in str:
        print( words,"(", len (words),")")

str = "Hello World How are you ?"
splitString(str)