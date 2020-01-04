class Employee:
    def __init__(self):
        self.__id =0
        self.__name =""
        self.__gender =""
        self.__city =""
        self.__salary =0
    def getId(self ):
        return self.__id 
    def setId(self ):
        self.__id =id 

    def getName (self ):
        return self .__name 
    def setName (self ,name ):
        self.__name =name 

    def getGender(self):
        return self.__gender
    def setGender (self ,gender):
        self.__gender = gender

    def getCity(self):
        return self.__city
    def setCity(self,city):
        self.__city=city

    def getSalary(self ):
        return self.__salary
    def setSalary(self,salary):
        self.__salary =salary

def main():
    print("Enter Employee data: ")
    id= int (input("Enter ID\t"))
    name = input ("Enter Name \t")
    gender = input("Enter Gender:")
    city = input ("Enter city\t")
    salary = int (input("Enter Salary:"))
    
    e= Employee()
    e.setId(id)
    e.setName(name)
    e.setGender(gender)
    e.setCity(city)
    e.setSalary(salary)
    id2= e.getId()
    name2 =e.getName()
    gender2 = e.getGender()
    city2 = e.getCity()
    salary2 =e.getSalary()

    print("\nDisplaying Employee Data:")
    print("Id\t\t:",id2)
    print("Name \t:",name2)
    print("Gender\t:",gender2)
    print("City\t",city2)
    print("Salary\t",salary2)

if __name__ =="__main__":
    main()
