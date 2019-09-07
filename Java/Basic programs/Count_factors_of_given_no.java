import java.util.Scanner;
public class Count_factors_of_given_no
{
	private static Scanner s;

    public static void main(String[] args)
	{
		s = new Scanner(System.in);
		
	    System.out.print("Enter the number : ");
	    int x = s.nextInt(); 
	    System.out.println("Number of factors of is : " +result(x));
	} 		
	
	public static int result(int num) 
	{	
		int ctr = 0;
		for(int i=1; i<=(int)Math.sqrt(num); i++)
	    {
	        if(num%i==0 && i*i!=num)
	        {
	            ctr+=2;
	        } 
	        else if (i*i==num) 
	        {
	            ctr++;
	        }
	    }
	        return ctr;
	}
}
