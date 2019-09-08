import java.util.Scanner;
public class Find_cube_from_1_to_n
{
	public static void main(String[] args)
	{
		int n,i;

		System.out.print("Enter the last number for cube : ");
		Scanner s= new Scanner(System.in);
		
		n = s.nextInt();

		for(i=1;i<=n;i++)
		{
			System.out.println("Cube of " +i+" is : "+(i*i*i));     
		}
	}
}
