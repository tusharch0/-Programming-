import java .util.*;
public class main{
    public static int fact(int num)
    {
        int fact =1,i;
        for (i=1;i<=num;i++)
        {
            fact =fact *i;
        }
        return fact;
    }
    public static void main(String args [])
    {
        int n,r;
        Scanner s=new Scanner (System.in);
        System.out.print ("Enter n: ");
        n=s.nextInt ;
        System.out.print ("Enter r: ");
        r=s.nextInt ;
        System.out.print("Combination is "+(fact (n)/(fact (r))));
        System.out.print("Permutation is "+(fact (n)/(fact (n-r))));
    }
}