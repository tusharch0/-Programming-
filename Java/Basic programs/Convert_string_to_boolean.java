import java.util.Scanner;
public class Convert_string_to_boolean
{
	private static Scanner s;

    public static void main(String[] args) 
	{
		s = new Scanner(System.in);

		System.out.print("Enter the string here : ");

		String str =s.next();

		Boolean blnObj1 = new Boolean(str);
		System.out.println("Boolean value is : " +blnObj1);
	}  
}
