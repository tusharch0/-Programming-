import java.util.Scanner;

public class Calculate_compound_interest 
{
	private static Scanner s;

	public static void main(String args[])
	{
		// declare and initialize here.
		double A=0,Pri,Rate,Time,t=1,CI;
		
		s = new Scanner(System.in);
		
		// enter principal, rate, time here
		System.out.print("Enter Principal : ");
		Pri=s.nextFloat();
		
		System.out.print("Enter Rate : ");
		Rate=s.nextFloat();
		
		System.out.print("Enter Time : ");
		Time=s.nextFloat();
		
		Rate=(1 + Rate/100);
		for(int i=0;i<Time;i++)
			t*=Rate;
		
		A=Pri*t;
		System.out.print("Amount : " +A);
		CI=A-Pri;
		System.out.print("\nCompound Interest : " +CI);	
	}
}
