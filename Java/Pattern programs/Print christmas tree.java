public class main
{
	public static final int SEGMENTS = 4;
	public static final int HEIGHT = 4;
	public static void main(String[] args)
	{
		makeTree();
	}

	public static void makeTree()
	{
		int maxStars = 2*HEIGHT+2*SEGMENTS-3;
		String maxStr = "";
		for (int len=0; len < maxStars; len++)
		{
			maxStr+=" ";
		}

		for (int i=1; i <= SEGMENTS; i++)
		{
			for (int line=1; line <= HEIGHT; line++)
			{
				String starStr = "";
				for (int j=1; j <= 2*line+2*i-3; j++)
				{
					starStr+="*";
				}

				for (int space=0; space <= maxStars-(HEIGHT+line+i); space++)
				{
					starStr = " " + starStr;
				}
				System.out.println(starStr);
			}
		}

		for (int i=0; i <= maxStars/2;i++)
		{
			System.out.print(" ");
		}
		
		System.out.print("*\n");
		
		for (int i=0; i <= maxStars/2;i++)
		{
			System.out.print(" ");
		}
		
		System.out.print("*\n");
		for(int i=0; i <= maxStars/2-3;i++)
		{
			System.out.print(" ");
		}
		System.out.print("*******\n");
	}
}
