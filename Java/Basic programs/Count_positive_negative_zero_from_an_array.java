import java.util.Scanner;
public class Count_positive_negative_zero_from_an_array
{
    private static Scanner s;

    public static void main(String args[])
    {
        int n,positive=0, negative=0, zero=0, i;
        int arr[] = new int[50];
        s = new Scanner(System.in);
       
        System.out.print("How many Number you want to Enter : ");
        n = s.nextInt();
		
        System.out.println("Enter " +n+ " Numbers : ");
      
        for(i=0; i<n; i++)
        {
            arr[i] = s.nextInt();
        }
        for(i=0; i<n; i++)
        {
            if(arr[i] < 0)
            {
                negative++;
            }
            else if(arr[i] == 0)
            {
                zero++;
            }
            else
            {
                positive++;
            }
        }
        System.out.print("Positive Numbers are: " + positive );
        System.out.print("\nNegative Numbers are: " + negative );
        System.out.print("\nZeros are: " + zero );
    }
}
