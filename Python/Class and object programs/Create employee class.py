class Employee :
    __id = 0
    __name=""
    __gender =""
    __city=""
    __salary=0

    def setData(self,id ,name ,gender ,city,salary):
        self.__id=id
        self.__name=name
        self.__gender=gender
        self.__city=city
        self.__salary=salary

    def showData(self):
        print("ID\t",self.__id )
        print("Name\t",self.__name )
        print("Gender \t",self.__gender)
        print("City\t",self.__city)
        print("Salary \t",self.__salary )

def main():
    emp =Employee()
    emp.setData(1,'tushar','male','delhi',55000)
    emp.showData()

if __name__ =="__main__":
    main()