import java.util.Scanner;

public class Check_given_no_is_harshad_no_or_not 
{
	private static Scanner sc;

    public static void main(String args[])
    {
        sc = new Scanner(System.in);
         
        System.out.print("Enter the number to check : ");
        int n = sc.nextInt();
        int c = n, d, sum = 0;
         
        while(c>0)
        {
            d = c%10;
            sum = sum + d;
            c = c/10;
        }
         
        if(n%sum == 0)
            System.out.println(n+" is a Harshad Number.");
        else
            System.out.println(n+" is not a Harshad Number.");      
    }
}
