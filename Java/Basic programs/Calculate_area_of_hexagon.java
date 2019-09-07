import java.util.Scanner;
public class Calculate_area_of_hexagon 
{
	private static Scanner sc;

    public static void main(String[] args) 
	{
		sc = new Scanner(System.in);
	
		System.out.print("Input the length : ");
		double s = sc.nextDouble();
		System.out.print("The area of the hexagon is : " + hexagonArea(s)+"\n");
	}

	public static double hexagonArea(double s)
	{
	    return (6*(s*s))/(4*Math.tan(Math.PI/6));
	}
}
