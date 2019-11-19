//Hierarchical Inheritance
class one
{
  public void print_One()
  {
    System.out.println("One");
  }
}
 
class two extends one
{
  public void print_Two()
  {
    System.out.println("Two");
  }
}
 
class three extends one
{
  /*............*/
}
 
// Derived class
public class HierarchicalInheritanceDemo
{
  public static void main(String[] args)
  {
    three g = new three();
    g.print_One();
    two t = new two();
    t.print_Two();
    g.print_One();
  }
}
