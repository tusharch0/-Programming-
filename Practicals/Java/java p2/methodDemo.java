
public class methodDemo {
    public String uid;
    public String name;
    public String dept;
    public String age ;

    public methodDemo(String uid,String name,String dept,String age)
    {
        this.uid=uid;
        this.name=name ;
        this.dept=dept;
        this.age=age;
    }
    
    public static void displayInfo()
    {   
        System.out.println("Static Method");
    }
    public void display()
    {
        System.out.println(uid);
        System.out.println(name);
        System.out.println(dept);
        System.out.println(age);
    }
}
