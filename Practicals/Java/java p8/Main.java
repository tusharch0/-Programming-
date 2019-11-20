import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;
 
class testserial implements Serializable {
  public int Srollno;
  public String Sname;
  
  public testserial(int Srollno,String Sname)
  {
    this.Srollno=Srollno;
    this.Sname=Sname;
  }
 
}
 
public class Main{
  public static void main(String[] args) throws Exception
  {
    //serialize();
    deserialize();
  }
  public static void serialize() throws Exception
  {
    testserial ts=new testserial(23,"Tushar");
    FileOutputStream fos=new FileOutputStream("D:\\FileWrite.ser");
    ObjectOutputStream oos=new ObjectOutputStream(fos);
    oos.writeObject(ts);
    oos.close();
    System.out.println("Success!!!");
  }
 
  public static void deserialize() throws Exception
  {
    FileInputStream fis=new FileInputStream("D:\\FileWrite.ser");
    ObjectInputStream ois=new ObjectInputStream(fis);
    testserial tsnew= (testserial)ois.readObject();
    fis.close();
    ois.close();
    
    System.out.println("Success!!!");
    System.out.println("Student Roll No.: "+tsnew.Srollno);
    System.out.println("Student Name: "+ tsnew.Sname);
  }
}
 
