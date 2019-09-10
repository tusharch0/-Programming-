import java.util.Scanner;
import java.util.InputMismatchException;

class StudentManagement extends Exception
{  
    private static final long serialVersionUID = 1L;

    StudentManagement(String error)
    {
		super(error);
	}
}

public class Exception_handling_Read_marks_between_1_to_100
{    
	private static Scanner kB;

    public static void main(String arg[])
    { 
		try
		{
			kB = new Scanner(System.in);
			
			System.out.print("Enter marks here : ");
			int h=kB.nextInt();
			
			if(!(h>=0 && h<=100))
			{
				throw(new StudentManagement("Invalid marks:"+h));
			}
			
			System.out.print("Entered marks are : " + h);			
			
		}
		catch(InputMismatchException e)
		{
			System.out.println("Invalid Input..Pls Input Integer Only..");
		}
		catch(StudentManagement e)
		{
			System.out.println("Error:"+e);
		}
	}
}
