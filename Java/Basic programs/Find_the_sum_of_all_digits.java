import java.util.Scanner;
public class Find_the_sum_of_all_digits
{
    private static Scanner s;

    public static void main(String args[])
    {
        int num, rem=0, sum=0, temp;
        s = new Scanner(System.in);
		
        System.out.print("Enter the Number : ");
        num = s.nextInt();
		
        temp = num;
		
        while(num>0)
        {
            rem = num%10;
            sum = sum+rem;
            num = num/10;
        }
		
        System.out.print("Sum of Digits of " +temp+ " is : " +sum);        
    }
}
