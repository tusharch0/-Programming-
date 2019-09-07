import java.util.Scanner;

public class Compare_two_number_with_each_other
{
	private static Scanner s;

    public static void main( String args[] )    
    {
        s = new Scanner(System.in);
        int number1;        
        int number2;   
      
        System.out.print("Enter first number : " );        
        number1 = s.nextInt();    
 
        System.out.print("Enter second number : " );         
        number2 = s.nextInt();               
        
        if ( number1 == number2 )           
            System.out.printf( "%d == %d\n", number1, number2 );  
        if ( number1 != number2 )          
            System.out.printf( "%d != %d\n", number1, number2 );  
        if ( number1 < number2 )          
            System.out.printf( "%d < %d\n", number1, number2 );  
        if ( number1 > number2 )          
            System.out.printf( "%d > %d\n", number1, number2 );  
        if ( number1 <= number2 )          
            System.out.printf( "%d <= %d\n", number1, number2 );  
        if ( number1 >= number2 )          
            System.out.printf( "%d >= %d\n", number1, number2 );  
    }
}
