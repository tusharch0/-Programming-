import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Find_perimeter_of_a_rectangle 
{
	public static void main(String[] args)
	{     
		int width = 0;
		int length = 0;
		try
		{
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

			System.out.print("Enter length of the rectangle : ");
			length = Integer.parseInt(br.readLine());

			System.out.print("Enter width of the rectangle : ");
			width = Integer.parseInt(br.readLine());       
		}
		catch(NumberFormatException ne)
		{
			System.out.print("Invalid value" + ne);
			System.exit(0);
		}
		catch(IOException ioe)
		{
			System.out.println("IO Error :" + ioe);
			System.exit(0);
		}
		
		int perimeter = 2 * (length + width);
		System.out.print("Perimeter of a rectangle is : " + perimeter);
	}
}
