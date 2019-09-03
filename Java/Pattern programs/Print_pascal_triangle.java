import java.util.Scanner;

public class Print_pascal_triangle
{
	public static void main(String[] args) 
	{
		
		int lib,p,q,r,x;

		Scanner s=new Scanner(System.in);

		System.out.print("Enter the rows : ");
		r=s.nextInt();
		lib=1;  
		q=0;

		System.out.println("Pascal's Triangle : ");

		while(q<r)
		{
			for(p=40-3*q;p>0;--p)
			System.out.print(" ");
			for(x=0;x<=q;++x)
			{
				if((x==0)||(q==0))
					lib=1;
				else
					lib=(lib*(q-x+1))/x;
				System.out.print("      ");
				System.out.print(lib);
			}
			System.out.println("");
			++q;
		}
	}
}
