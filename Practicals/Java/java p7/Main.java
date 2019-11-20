import java.io.*;
class Main
{
 public static void main(String[] args) throws Exception
 {
   FileWriter fw = new FileWriter("D:\\javatest.txt");
   FileReader fr = new FileReader("D:\\javatest.txt");
 
   fw.write("Hello!Welcome to JAVA programming.");
 
   int i;
   while((i=fr.read())!=-1)
   {
     System.out.println((char) i);
   }
   fr.close();
   fw.close();
   System.out.println("Success!");
 
 }
}
