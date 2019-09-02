import java.util.*;
class Swap_two_number_without_using_third_variable
{
	public static void main(String []s)
	{
		int a,b;
		Scanner sc =new Scanner(System.in);

		System.out.print("Enter value of a: ");
		a=sc.nextInt();
		System.out.print("Enter value of a: ");
		b=sc.nextInt();

		System.out.println("Before swapping  a: "+ a +", b: " + b);
		a=a+b;
		b=a-b;
		a=a-b;
		System.out.println("After swapping  a: "+ a +", b: " + b);
	}
}
