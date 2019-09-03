import java.util.Scanner;
public class Print_pattern_of_alphabets
{
	public static void main(String[] args) 
	{
		int alphabet=65;

		Scanner sc = new Scanner(System.in);

		System.out.print("Enter number of rows: ");

		int rows = sc.nextInt();

		System.out.println("Here is your pattern....!!!");

		for(int i=1;i<rows;i++)
		{            
			for(int j=1;j<=i;j++)
			{
				System.out.print((char)alphabet);
				alphabet++;
			}
			System.out.println();
		}
		sc.close();
	}
}
