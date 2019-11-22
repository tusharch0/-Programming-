class Main {
    public static void main(String args[]) {
        int num1, num2;
        try {
            num1 = 0;
            num2 = 62 / num1;
            System.out.println(num2);
            System.out.println("Hey I'm at the end of try block");
            throw new ArithmeticException();
        }
  
        catch (ArithmeticException e) {
            System.out.println("You should not divide a number by zero");
        }
  
        catch (Exception e) {
  
            /* This is a generic Exception handler. This will execute if the exception is not handled by previous catch blocks.*/
  
            System.out.println("Exception occurred");
        }
        System.out.println("I'm out of try-catch block in Java.");
    }
 }
 