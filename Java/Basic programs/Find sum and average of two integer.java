import java.util.*;
class main{
    public static void main(String args[])
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