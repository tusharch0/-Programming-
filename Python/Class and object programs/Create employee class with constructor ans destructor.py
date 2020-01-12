class Employee :
    def __init__(self):
        self.__id =0
        self.__name =""
        self.__gender =""
        self.__city =""
        self .__salary =""
        print("Object Initialized.")
    def __del__(self):
        print("Object Destroyed.")
    def setData(self):
        self.__id = int(input("Enter ID\t"))
        self.__name = input("Enter Name \t:")
        self.__gender = input("Enter gender: ")
        self.__city = input("Enter city :")
        self.__salary = int (input ("Enter salary :"))
    def __str__(self ):
        data = "["+str(self.__id)+","+self.__name +","+self.__gender+","+self.__city+","+self.__salary+"]" 
        return data
    def showData(self ):
        print("ID \t",self.__id)
        print("Name \t",self.__name )
        print("Gender \t",self.__gender )
        print("City\t",self.__city)
        print("salary \t",self.__salary)

def main():
    emp=Employee ()
    emp.setData()
    emp.showData()
    print(emp)

if __name__=="__main__":
    main()