import java.util.Scanner;

public class Generate_random_number
{
	private static Scanner sc;

    public static void main( String args[] )
	{ 
		sc = new Scanner( System.in ); 

		System.out.print("Enter starting range : "); 

		int rsnum = sc.nextInt(); 

		System.out.print("Enter final range : "); 

		int renum = sc.nextInt(); 

		int random_num = rsnum + (int)(Math.random() * ((renum - rsnum) + 1));
		System.out.println("Random number between given range : " +random_num);
	}  
}
