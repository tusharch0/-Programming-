import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Check_given_no_is_emrip_or_not
{
	static BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
	int n, rev, f;

	Check_given_no_is_emrip_or_not(int nn) 
	{
		n=nn;
		rev=0;
		f=2;
	}

	int isprime(int x) 
	{
		if(f<=x)
		{
			if(x%f!=0) 
			{
				f++;
				isprime(x);
			}
		}

		if(f==x)
			return 1;
		else
			return 0;
	}

	void isEmirp()
	{
		int copy=n, d;
		
		while(copy>0) 
		{
			d=copy%10;
			rev=rev*10+d;
			copy=copy/10;
		}
		
		
		int a=isprime(n); 
		f=2; 
		int b=isprime(rev); 
		
		if(a==1 && b==1)
			System.out.println(n+" is an Emirp Number");
		else
			System.out.println(n+" is Not an Emirp Number");
	}

	public static void main(String args[])throws IOException
	{
		System.out.print("Enter the number : ");
		
		int n=Integer.parseInt(br.readLine());
		
		Check_given_no_is_emrip_or_not ob=new Check_given_no_is_emrip_or_not(n);
		ob.isEmirp();
	}    
}
