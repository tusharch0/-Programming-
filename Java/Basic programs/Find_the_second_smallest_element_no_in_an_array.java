import java.util.Scanner;

public class Find_the_second_smallest_element_no_in_an_array
{
    private static Scanner sc;

    public static void main(String[] args) 
    {
        int n, min;
        sc = new Scanner(System.in);
        
        System.out.print("Enter number of elements : ");
        n = sc.nextInt();
        
        int a[] = new int[n];
        
        System.out.println("Enter the elements in array : ");
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
                    min = a[i];
                    a[i] = a[j];
                    a[j] = min;
                }
            }
        }
        System.out.println("The Smallest element in the array is :"+a[1]);
    }
}
