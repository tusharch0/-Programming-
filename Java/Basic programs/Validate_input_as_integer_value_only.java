import java.util.Scanner;
import java.util.InputMismatchException;
public class Validate_input_as_integer_value_only
{   
	private static Scanner s;

    // create function readint for reading input value.
	public static int readInt(String msg)
	{ 
		boolean error=false;
		int x=0;
		do
		{
			try
			{
				s = new Scanner(System.in);

				// enter here.
				System.out.print("Enter integer : ");
				x=s.nextInt();
				error=false;
			}
			catch(InputMismatchException e)
			{
				// accept integer only.
				System.out.println("Invalid Input..Pls Input Integer Only..");
				error=true;
			}
		}
		while(error);
		return(x);
	}
}
