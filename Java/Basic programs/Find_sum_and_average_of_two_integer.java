import java.util.*;
class Find_sum_and_average_of_two_integer
{
    public static void main (String args[])
    {
        int a,b,sum;
        float avg;
        Scanner s=new Scanner(System.in);
        System.out.println("Enter first no. ");
        a=s.nextInt();
        System.out.println("Enter second no. ");
        b=s.nextInt();
        sum=a+b;
        avg =(float)(sum/2);
        System.out.println("Sum : "+sum+"Avg : "+avg);
    }
}