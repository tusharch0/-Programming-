//Overriding
class Dog{
    public void bark(){
        System.out.println("woof ");
    }
}
class Hound extends Dog{
    public void sniff(){
        System.out.println("sniff ");
    }
 
    public void bark(){
        System.out.println("bowl");
    }
}
 
public class Main{
    public static void main(String [] args){
        Dog dog = new Hound();
        dog.bark();
    }
}
