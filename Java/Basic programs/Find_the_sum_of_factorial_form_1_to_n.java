import java.util.Scanner;
public class Find_the_sum_of_factorial_form_1_to_n
{
	private static Scanner sc;

    public static void main(String[] args)
	{
		sc = new Scanner(System.in);
		
		System.out.print("Enter number : ");
		int n = sc.nextInt();
 
		int total=0;
 
		int i=1;
		
		while(i <= n) 
		{
			int factorial=1;
			int j=1;
			
			while(j <= i) 
			{
				factorial=factorial*j;
				j = j+1;
			}
			total = total + factorial;
			i=i+1;
		}
		System.out.println("Sum : " + total);
	}
}
