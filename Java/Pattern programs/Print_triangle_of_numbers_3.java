import java.util.Scanner;
public class Print_trangle_of_numbers_3
{
	public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
         
        System.out.print("Enter row for pattern : ");
         
        int rows = sc.nextInt();
         
        System.out.println("Here is your pattern....!!!");
        
        for (int i = rows; i >= 1; i--) 
        {
            for (int j = 1; j <= i; j++)
            {
                System.out.print(j+" ");
            }      
            System.out.println();
        }
        
        for (int i = 2; i <= rows; i++) 
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
