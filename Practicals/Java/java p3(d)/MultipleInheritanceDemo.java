//Multiple Inheritance (using Interface)
interface one 
{ 
public void print_First(); 
} 
 
interface two 
{ 
public void print_Second(); 
} 
 
interface three extends one,two 
{ 
public void print_third(); 
} 
class child implements three 
{ 
@Override
public void print_First() { 
System.out.println("First"); 
} 
 
public void print_Second() 
{ 
System.out.println("Second"); 
} 
public void print_Third() { 
    System.out.println("Third"); 
    }

@Override
public void print_third() {
	// TODO Auto-generated method stub
	
} 
} 
 
// Derived class 
public class MultipleInheritanceDemo 
{ 
public static void main(String[] args) 
{ 
child c = new child(); 
c.print_First(); 
c.print_Second(); 
c.print_Third(); 
} 
} 
