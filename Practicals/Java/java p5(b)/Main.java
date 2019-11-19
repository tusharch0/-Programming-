class Main{
    public void bark(){
        System.out.println("woof ");
    }
 
    //overloading method
    public void bark(int num){
    	for(int i=0; i<num; i++)
    		System.out.println("woof ");
    }

		public static void main(String[]args){
			Main obj= new Main();
			obj.bark();
			obj.bark(4);
		}
}
