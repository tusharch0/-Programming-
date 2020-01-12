class Student :
    counter = 0
    def __init__(self ,name ,age):
        self.name = name 
        self.age = age 
        Student.counter +=1
    def printDetails (self):
        print(self.name,self.age,"years old")

student1= Student('Tushar',20)
student2= Student('Rohit',32)
student3= Student('Virat',40)
print("Total number of object created :",Student.counter)