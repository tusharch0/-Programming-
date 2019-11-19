//different type of constructure in java
class ConstructorDemo
{
	private String uid;
	private String name ;
	private String dept;
	private String fee;

  ConstructorDemo()
	{
		uid="18bcs6523";
		name="Tushar";
		dept="CSE";
		fee="45000";
	}
	ConstructorDemo(String name,String uid,String dept,String fee)
	{
		this.uid=uid;
		this.name =name ;
		this.dept=dept;
		this.fee=fee;
	}
	void displayInfo()
	{
    System.out.println(uid );
		System.out.println(name);
		System.out.println(dept);
		System.out.println(fee);
	}
	public static void main(String args[])
	{
		ConstructorDemo cd=new ConstructorDemo();
		cd.displayInfo();
	}

}