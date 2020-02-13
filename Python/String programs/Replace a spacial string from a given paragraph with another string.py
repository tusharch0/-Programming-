import re 
paragraph ='''these days the coders are the best '''

reg= re.compile('coders')
s=reg.sub("students",paragraph)
print(s)