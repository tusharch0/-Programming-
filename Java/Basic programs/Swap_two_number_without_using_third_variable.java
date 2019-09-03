import java.util.*;
class Swap_two_number_without_using_third_variable
{
	private static Scanner sc;

	public static void main(String []s)
	{
		int a,b;
		sc = new Scanner(System.in);

		System.out.print("Enter value of a: ");
		a=sc.nextInt();
		System.out.print("Enter value of b: ");
		b=sc.nextInt();

		System.out.println("Before swapping  a: "+ a +", b: " + b);
		a=a+b;
		b=a-b;
		a=a-b;
		System.out.println("After swapping  a: "+ a +", b: " + b);
	}
}