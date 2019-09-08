import java.util.Scanner;

public class Print_triangle_of_numbers_2 
{
	public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
         
        System.out.print("Enter row for pattern : ");
         
        int rows = sc.nextInt();
        
        System.out.println("Here is your pattern....!!!");
         
        for (int i = 1; i <= rows; i++) 
        {
            for (int j = 1; j <= i; j++)
            {
                System.out.print(j+" ");
            }            
            System.out.println();
        }
        sc.close();
    }
}
