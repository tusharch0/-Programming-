# Grade of the Student marks out of five subject
a= int (input ("Enter the marks of subject 1 : "))
b= int (input ("Enter the marks of subject 2 : "))
c= int (input ("Enter the marks of subject 3 : "))
d= int (input ("Enter the marks of subject 4 : "))
e= int (input ("Enter the marks of subject 5 : "))

avg = (a+b+c+d+e)/5
print(avg)
if (avg>85):
    print("Grade is A")
elif(avg>70):
    print("Grade is B")
elif (avg >60):
    print("grade is C")
elif (avg>50):
    print("Grade is D")
elif(avg >40):
    print("Grade is E")
else:
    print("Grade is F")