import java.util.Scanner;

public class Check_character_is_alphabet_or_not
{
    private static Scanner s;

    public static void main(String args[])
    {
        char ch;
        s = new Scanner(System.in);
		
        System.out.print("Enter a Character : ");
        ch = s.next().charAt(0);
		
        if((ch>='a' && ch<='z') || (ch>='A' && ch<='Z'))
        {
            System.out.print(ch + " is an Alphabet");
        }
        else
        {
            System.out.print(ch + " is not an Alphabet");
        }
    }
}
