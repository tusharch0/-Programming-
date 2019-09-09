import java.util.*;
class Find_correct_output_of_student
{
	// creating array object.
    char A[][],K[];
    int S[],n;
    private Scanner sc;
     
    void input()
    {
    	sc = new Scanner(System.in);
        
        // enter number of participants.
        System.out.print("Enter number of participants : ");
        n = sc.nextInt();
        
        // condition of least and heighest input
        if(n<4 || n>10)
        {
        	// input the range here.
            System.out.print("Input size out of range : ");
            System.exit(0);
        }
        
        A = new char[n][5]; 
        K = new char[5]; 
        S = new int[n]; 
        
        // enter the correct answer to check the answers of students.
        System.out.println("\n* Enter answer of each participant row-wise in a single line *\n");
        for(int i = 0; i<n; i++)
        {
            System.out.print("Participant "+(i+1)+" : ");
            for(int j=0; j<5; j++)
            {
                A[i][j] = sc.next().charAt(0);
            }
        }
        System.out.print("\nEnter Answer Key : ");
        for(int i = 0; i<5; i++)
        {
            K[i] = sc.next().charAt(0);
        }
    }
 
    // Function to calculate score of participant
    void Score() 
    {
 
        for(int i = 0; i<n; i++)
        {
            S[i] = 0;
            for(int j=0; j<5; j++)
            {
            	// Checking if Answer of the participants match with the key or not
                if(A[i][j] == K[j]) 
                {
                    S[i]++;
                }
            }
        }
    }
 
    // function to print score.
    void printScore()
    {
        int max = 0;
        System.out.println("\nSCORES : ");
        for(int i = 0; i<n; i++)
        {
            System.out.println("\tParticipant "+(i+1)+" = "+S[i]);
            if(S[i]>max)
            {
            	// Storing the Highest Score
                max = S[i]; 
            }
        }
        System.out.println();
         
        System.out.println("\tHighest Score : "+max);
         
        // Printing all those participant number who got highest score
        System.out.println("\tHighest Scorers : ");
        for(int i = 0; i<n; i++) 
        {
            if(S[i] == max)
            {
                System.out.println("\t\t\tParticipant "+(i+1));
            }
        }
    }
 
    public static void main(String args[])
    {
    	Find_correct_output_of_student ob = new Find_correct_output_of_student();
        ob.input();
        ob.Score();
        ob.printScore();
    }
}
