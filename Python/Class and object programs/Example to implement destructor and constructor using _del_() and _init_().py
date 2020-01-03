class Employee :
    def __init__(self ):
        self.__id =0
        self.__name =""
        self.__gender =""
        self.__city=""
        self.__salary=0
        print("Object Initialized")
    def __del__(self ):
        print("Object Destroyed")
    def setData(self):
        self.__id =int(input ("Enter ID"))
        self.__name = input("Enter Name ")
        self.__gender = input("Enter Gender ")
        self.__city = input("Enter city")
        self.__salary = int(input ("Enter salary"))
    def showData(self):
        print ("Id\t",self.__id)
        print("Name \t",self.__name)
        print("Gender \t",self.__gender)
        print("City\t",self.__city)
        print("Salary\t",self.__salary)

def main():
    emp = Employee ()
    emp.showData()

if __name__ =="__main__":
    main()