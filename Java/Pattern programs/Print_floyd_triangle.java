import java.util.Scanner;
public class Print_floyd_triangle
{
    private static Scanner s;

    public static void main(String args[])
    {
	
        int rows, i, j, k=1;
        s = new Scanner(System.in);
		
        System.out.print("Enter rows u want : ");
        rows = s.nextInt();
		
        System.out.print("Floyd's Triangle :\n");
        for(i=1; i<=rows; i++)
        {
            for(j=1; j<=i; j++, k++)
            {
                System.out.print(k + " ");
            }
            System.out.println();			
        }
    }
}
