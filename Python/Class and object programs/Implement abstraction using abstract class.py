class Vehicle:
    def start(self, name =""):
        print (name ,"is Started ")
    def acclerate(self,name =""):
        pass
    def park(self,name ="" ):
        pass
    def stop(self ,name =""):
        print(name ,"is stopped")

class Bike (Vehicle ):
    def acclerate(self,name =""):
        print(name ,"is accelrating @ 60kmph")
    def park(self,name= ""):
        print(name ,"is parked at two wheeler parking")

class Car(Vehicle):
    def acclerate(self,name=""):
        print(name ,"is accelrating @ 90kmph")
    def park(self,name =""):
        print (name ,"is parked at four wheeler parking ")

def main():
    print("Bike Object ")
    b=Bike()
    b.start("Bike ")
    b.acclerate("Bike")
    b.park("Bike")
    b.stop("Bike ")

    print("Car object ")
    c= Car()
    c.start("Car ")
    c.acclerate("Car")
    c.park("Car")
    c.stop("Car")
if __name__=="__main__":main()