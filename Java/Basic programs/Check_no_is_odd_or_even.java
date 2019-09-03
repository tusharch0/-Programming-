import java.util.*;
public class Check_no_is_odd_or_even
{
	private static Scanner s;

	public static void main(String args[])
	{
		s = new Scanner(System.in);
		int num;

		System.out.print("Enter an integer number: ");
		num=s.nextInt();
		
		if(num%2 ==0)
		{
			System.out.println(num +" is an EVEN number.");
		}
		else
		{
			System.out.println(num +" is an ODD number.");
		}
	}
}
