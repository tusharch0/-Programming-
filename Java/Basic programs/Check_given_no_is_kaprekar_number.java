public class Check_given_no_is_kaprekar_number 
{
	public static void main(String[] args)
	{
		int ctr = 0;
		int base = (args.length > 0) ? Integer.parseInt(args[0]) : 10;

		for(long n = 1; n <= 1000; n++)
		{
			String St = Long.toString(n * n, base);

			for(int j = 0; j < St.length() / 2 + 1; j++)
			{
				String[] S = split_num(St, j);

				long N1 = Long.parseLong(S[0], base);
				long N2 = Long.parseLong(S[1], base);

				if(N2 == 0) break;

				if(N1 + N2 == n)
				{
					System.out.println(Long.toString(n, base) +"\t" + St + "\t  " + S[0] + " + " + S[1]);
					ctr++;
					break;
				}
			}
		}
		System.out.println(ctr + " Kaprekar numbers.");
		}

		private static String[] split_num(String str, int idx)
		{
		String[] A1 = new String[2];
		A1[0] = str.substring(0, idx);

		if(A1[0].equals("")) A1[0] = "0"; 
		A1[1] = str.substring(idx);
		return A1;
	}	
}
