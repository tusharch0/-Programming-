import java.util.Scanner;

public class Find_the_mean_of_given_number
{
    private static Scanner s;

    public static void main(String args[])
    {
        int n, i, sum=0, mean;
        int arr[] = new int[50];
        s = new Scanner(System.in);
		
        System.out.print("How many Number you want to Enter : ");
        n = s.nextInt();
		
        System.out.println("Enter " +n+ " Numbers : ");
      
        for(i=0; i<n; i++)
        {
            arr[i] = s.nextInt();
            sum = sum + arr[i];
        }
        mean = sum/n;
        System.out.print("Mean of the given numbers is : " +mean);
    }
}
