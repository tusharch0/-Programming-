import java.util.Scanner;

public class Find_the_length_of_string
{
	private static Scanner s;

	public static void main(String[] args)
	{
		String text;
		s = new Scanner(System.in);

		System.out.print("Enter the string : ");
		text=s.nextLine();

		int length = text.length();
		System.out.println("Length of the given string " + text+ " is : " +length );
	}
}
