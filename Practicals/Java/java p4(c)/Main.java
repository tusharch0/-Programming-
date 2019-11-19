//private
class A
{
 private void display()
  {
    System.out.println("now you can Access");
  }
}
 
class Main
{
public static void main(String args[])
  {
    A obj = new A();
    obj.display();
  }
}
