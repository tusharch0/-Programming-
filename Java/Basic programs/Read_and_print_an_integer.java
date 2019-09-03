import java.util.*;
class Read_and_print_an_integer
{
    private static Scanner s;

    public static void main(String args[])
    {
        int a;
        s = new Scanner(System.in);
        a=s.nextInt();
        System.out.println("Value of a : "+a);
    }
}