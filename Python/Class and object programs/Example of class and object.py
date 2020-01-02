class Message (object):
    def __init__(self):
        self.msg =None

    def assignValue(self):
        self.msg = "Hello World "

    def getValue (self,str):
        self.msg =str

    def printValue(self):
        print("msg = ",self.msg)

M= Message ()
print ("Value after init . the object ...")
M.printValue ();
M.assignValue()
print("value after assignValue()...")
M.printValue();
M.getValue("How are you ?")
print("Value after getValue()...")
M.printValue();