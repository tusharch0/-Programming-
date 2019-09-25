import java.util.Scanner;

public class Find_the_second_largest_no_in_an_array 
{
    private static Scanner sc;

    public static void main(String[] args) 
    {
        int n, max;
        sc = new Scanner(System.in);
        
        System.out.print("Enter total number of elements you wants : ");
        n = sc.nextInt();
        int a[] = new int[n];
        
        System.out.println("Enter all the elements:");
        for (int i = 0; i < n; i++) 
        {
            a[i] = sc.nextInt();
        }
        for (int i = 0; i < n; i++) 
        {
            for (int j = i + 1; j < n; j++) 
            {
                if (a[i] > a[j]) 
                {
                    max = a[i];
                    a[i] = a[j];
                    a[j] = max;
                }
            }
        }
        System.out.println("The Second Largest Elements in the Array is :"+a[n-2]);
    }
}
