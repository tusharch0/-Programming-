public class Print_uppercase_and_lower_case_alphabets
{
	public static void main(String args[])
	{
		char ch;

		System.out.println("Uppercase alphabets:");
		for(ch='A';ch<='Z';ch++)
        {
			System.out.print(ch + " ");
        }
        
		System.out.println("");
 
		System.out.println("Lowercase alphabets:");
		for(ch='a';ch<='z';ch++)
        {
			System.out.print(ch + " ");	
        }	
	}
}
