word =str(input ("Enter a string :"))
Guess =['a','e','i','k','m','s']
flag=0
for i in word:
    if i in Guess:
        flag+=1
if len(word)==flag:
    print("Completly In")
else :
    print("Not In")

print(flag,'matches')