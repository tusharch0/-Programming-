class  Details1:
    def __init__(self ):
        self .__id=0
    def setId(self):
        self .__id =int (input ("Enter ID "))
    def showId(self):
        print ("Id : ",self.__id )

class Details2(Details1):
    def __init__(self ):
        self .__name =""
    def setName (self):
        self .setId()
        self .__name = input ("Enter Name :")
    def showName (self ):
        self.showId()
        print("Name : ",self.__name )

class Details3(Details2):
    def __init__(self):
        self.__gender =""
    def setGender (self ):
        self .setName ()
        self .__gender = input("Enter Gender ")
    def showGender (self ):
        self .showName()
        print("Gender :",self.__gender )

class Employee (Details3):
    def __init__(self):
        self.__desig=""
        self.__dept =""
    def setEmployee(self ):
        self.setGender()
        self.__design = input ("Enter Designation :")
        self.__dept = input("Enter Department ")
    def showEmployee(self ):
        self .showGender()
        print ("Designation :",self .__desig)
        print ("Department :",self.__dept)

def main():
    e = Employee()
    e.setEmployee()
    e.showEmployee()

if __name__=="__main__":main()