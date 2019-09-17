import java.util.Scanner;
import java.util.InputMismatchException;
class Handle_mutiple_exceptions
{    
	private static Scanner sc;

    public static void main(String arg[])
    {  
		try
		{
			sc = new Scanner(System.in);
			
			System.out.print("Enter First Number : ");
			int x=sc.nextInt();

			System.out.print("Enter Second Number : ");
			int y=sc.nextInt();
			int z=x/y;
			
			System.out.println("Result:"+z);
		}
		catch(InputMismatchException e)
		{
			System.out.println("Invalid Input...");}
			catch(ArithmeticException e)
		{
			System.out.println("Error:Divide By ZERO");
		}
    }
}
