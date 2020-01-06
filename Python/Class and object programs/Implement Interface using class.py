import math 
class Shape:
    def input (self):
        pass
    def process(self):
        pass 
    def output (self):
        pass

class Circle (Shape ):
    def __init__(self ,rad=0.0):
        self.__radius =rad
        self.__area =0.0
    def input (self ):
        self .__radius =float (input ("Enter radius :"))
    def process(self ):
        self .__area=math.pi*math.pow(self.__radius,2)
    def output (self):
        print("Area : ",self.__area)

class Rectangle (Shape ):
    def __init__(self ,len=0,br=0):
        self .__length =len
        self .__breadth =br 
        self .__area=0
    def input (self):
        self.__length =int (input ("Enter Length :"))
        self.__breadth =int (input ("Enter breadth :"))
    def process(self):
        self.__area=self .__length*self.__breadth
    def output(self):
        print("Area :",self.__area)

def main():
    print("Circle Object :")
    c=Circle()
    c.input()
    c.process()
    c.output()

    print("\nRectangle Object :")
    r=Rectangle()
    r.input()
    r.process()
    r.output()
if __name__=="__main__":main()