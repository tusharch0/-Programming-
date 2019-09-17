import java.util.Scanner;

class Exception_handling_divide_two_no
{  
	private static Scanner s;

	public static void main(String arg[])
    {  
		try
		{
			int a,b,c;
			s = new Scanner(System.in);
			
			System.out.print("Enter first number : ");
			a=s.nextInt();
       
			System.out.print("Enter second number : ");
			b=s.nextInt();
       
			c=a/b;
			System.out.println("Result:"+c);
		}
		catch(ArithmeticException e)
		{
			System.out.println("Error:"+e.getMessage());
			System.out.println("Error:"+e);
		}
		System.out.println("End of Program...");
	}
}
