import java.util.Scanner;

public class Verify_answer_of_answer_sheets {
    char A[][], K[];
    int S[], n;
    private Scanner s2;

    void input() {
        s2 = new Scanner(System.in);

        System.out.print("Enter number of Students : ");
        n = s2.nextInt();

        if (n < 4 || n > 10) {
            System.out.println("INPUT SIZE OUT OF RANGE");
            System.exit(0);
        }
        A = new char[n][5];

        K = new char[5];

        S = new int[n];

        System.out.println("\n* Enter answer of each participant row-wise in a single line *\n");
        for (int i = 0; i < n; i++) {
            System.out.println("Participant " + (i + 1) + " : ");
            for (int j = 0; j < 5; j++) {
                A[i][j] = s2.next().charAt(0);
            }
        }

        System.out.println("\nEnter Answer Key : ");
        for (int i = 0; i < 5; i++) {
            K[i] = s2.next().charAt(0);
        }
    }

    void CalcScore() {
        for (int i = 0; i < n; i++) {
            S[i] = 0;
            for (int j = 0; j < 5; j++) {
                if (A[i][j] == K[j]) {
                    S[i]++;
                }
            }
        }
    }

    void printScore() {
        int max = 0;
        System.out.println("\nSCORES : ");
        for (int i = 0; i < n; i++) {
            System.out.println("\tParticipant " + (i + 1) + " = " + S[i]);
            if (S[i] > max) {
                max = S[i];
            }
        }
        System.out.println();

        System.out.println("\tHighest Score : " + max);

        System.out.println("\tHighest Scorers : ");

        for (int i = 0; i < n; i++) {
            if (S[i] == max) {
                System.out.print("\t\t\tParticipant " + (i + 1));
            }
        }
    }

    public static void main(String args[]) {
        Verify_answer_of_answer_sheets ob = new Verify_answer_of_answer_sheets();
		ob.input();
		ob.CalcScore();
		ob.printScore();
    }
    
}
