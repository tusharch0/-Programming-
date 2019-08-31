import java.util.Scanner;

public class main
{
    public static void main(String args[])
    {
        int n, n1, n2, i, rem, temp, count=0;
        Scanner scan = new Scanner(System.in);
        
        System.out.print("Enter Starting Number :  ");
        n1 = scan.nextInt();
        System.out.print("Enter Ending Number :  ");
        n2 = scan.nextInt();
        for(i=n1+1; i<n2; i++)
        {
            temp = i;
            n = 0;
            while(temp != 0)
            {
                rem = temp%10;
                n = n + rem*rem*rem;
                temp = temp/10;
            }
            if(i == n)
            {
                if(count == 0)
                {
                    System.out.print("Armstrong Numbers Between the Given Interval are : \n");
                }
                System.out.print(i + "  ");
                count++;
            }
        }
        if(count == 0)
        {
            System.out.print("Armstrong Number not Found between the Given Interval.");
        }
    }
}
