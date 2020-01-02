class person :
    def __init__(self):
        self.name ="XYZ"
        self.age =0
    def printValues(self):
        print("Name : ",self.name) 
        print("Age",self.age)

p = person()
p.printValues();
p.name = "Tushar"
p.age = 20
p.printValues();