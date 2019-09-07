import java.util.Scanner;
public class Print_triangle_of_numbers_1
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
         
        System.out.print("Enter rows here : ");
        int rows = sc.nextInt();
         
        System.out.println("Here is your pattern....!!!");
         
        for (int i = 1; i <= rows; i++) 
        {
          for (int j = 1; j < i; j++) 
            {
                System.out.print(" ");
            } 
          for (int j = i; j <= rows; j++) 
            { 
                System.out.print(j+" "); 
            }   
            System.out.println(); 
        } 
       
        for (int i = rows-1; i >= 1; i--) 
        {
          for (int j = 1; j < i; j++) 
            {
                System.out.print(" ");
            }  
          for (int j = i; j <= rows; j++)
            {
                System.out.print(j+" ");
            }   
            System.out.println();
        }
        sc.close();
    }
}
