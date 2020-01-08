class Personel :
    def __init__(self):
        self.__id =0
        self.__name =""
        self.__gender =""
    def setPersonel (self):
        self.__id=int(input("Enter ID: "))
        self.__name =input ("Enter Name :")
        self.__gender =input("Enter gender :")
    def showPersonel(self):
        print("Id : ",self.__id)
        print("Name : ",self.__name )
        print("Gender : ",self.__gender )

class Educational:
    def __init__(self ):
        self .__stream=""
        self .__year=""
    def setEducation(self ):
        self .__stream =input("Enter Stream: ")
        self .__year =input("Enter year : ")
    def showEducation (self ):
        print("Stream : ",self.__stream)
        print("year : ",self.__year)

class Student(Personel, Educational):
    def __init__(self ):
        self.__address =""
        self.__contact =""
    def setStudent (self ):
        self .setPersonel()
        self .__address= input("Enter Address : ")
        self .__contact = input("Enter contact : ")
        self .setEducation()

    def showStudent (self ):
        self.showPersonel()
        print("Address : ",self .__address )
        print ("Contact : ",self .__contact )
        self .showEducational()

def main():
    s=Student ()
    s.setStudent ()
    s.showStudent ()
if __name__=="__main()":
    main()