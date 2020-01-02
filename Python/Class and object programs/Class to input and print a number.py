class Number :
    def __init__(self,num):
        self.num = num ;
    def inputNum (self):
        self.num  = int (input ("Enter the integer number : "))
    def printNum(self ):
        print("num : ",self.num )

objN = Number (100);
objN.printNum()

objN.inputNum()
objN.printNum()