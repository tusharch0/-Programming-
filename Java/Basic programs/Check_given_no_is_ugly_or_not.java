import java.util.Scanner;

public class Check_given_no_is_ugly_or_not
{
	private static Scanner sc;

    public static void main(String[] args)
	{
		sc = new Scanner(System.in);

		System.out.print("Enter the number : ");
		int n = sc.nextInt();  		
		if (n <= 0)
		{
			System.out.print("Enter correct/+ve number.");
		}
		int x = 0;
		while (n != 1)
		{
			if (n % 5 == 0)
			{
				n /= 5;
			}

			else if (n % 3 == 0) 
			{
				n /= 3;
			}

			else if (n % 2 == 0)
			{
				n /= 2;
			}

			else
			{
				System.out.print("The given number is not a ugly number.");
				x = 1;
				break;
			}
		}
		if (x==0)
			System.out.print("The given number is an ugly number.");
		System.out.print("\n");
	}
}
