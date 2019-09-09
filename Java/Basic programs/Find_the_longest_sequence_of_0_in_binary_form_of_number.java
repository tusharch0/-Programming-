import java.util.*;
public class Find_the_longest_sequence_of_0_in_binary_form_of_number
{
private static Scanner sc;

public static void main(String args[])
{ 
  int num,quot,i=1,j;
  int bin_num[]=new int[100];
  sc = new Scanner (System.in);
  System.out.println("Enter the number: ");
  num=sc.nextInt();
  quot=num;
  while(quot !=0)
  {
      bin_num[i++]=quot%2;
  }
  String str="";
  System.out.print("Binary number is ");
  for(j=i-1;j>0;j--)
  {
      str=str+bin_num[j];
  }
  System.out.print(str);
  i=str.length()-1;
  while(str.charAt(i)=='0')
  {
      i--;
  }
  int length=0;
  int ctr=0;
  for(;i>=0;i-- )
  {  if (str.charAt(i)=='1')
  {
      length=Math.max(length,ctr);
      ctr=0;
  }
  else{
      ctr++;
  }
  }
  length=Math.max(length,ctr);
  System.out.println("\nLength of the longest sequence: "+length);
}
}
