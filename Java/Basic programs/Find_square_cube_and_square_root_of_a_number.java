import java.util.*;
public class Find_square_cube_and_square_root_of_a_number
{
	private static Scanner s;

	public static void main(String args[]){
		s = new Scanner(System.in);
		int num;

		System.out.print("Enter a number: ");
		num=s.nextInt();

		System.out.println("Square of "+ num + " is: "+ Math.pow(num, 2));
		System.out.println("Cube of "+ num + " is: "+ Math.pow(num, 3));
		System.out.println("Square Root of "+ num + " is: "+ Math.sqrt(num));
	}
}
