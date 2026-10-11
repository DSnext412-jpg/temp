import java.util.*;
class invalidage extends Exception{

invalidage(String s){
    super(s);
  } 
}

class driver
{
  int lno1,age1;
  String nm1,add1;
  driver(int lno,String nm,String add,int age){
    lno1=lno;
    nm1=nm;
    add1=add;
    age1=age;
  }
  void check(){
    try{
      if(age1<18)
        throw new invalidage("age is below 18");  
      else{
        System.out.println("Driver details");
        System.out.println(lno1+"  "+nm1+"  "+add1+"  "+age1);
      }
    }catch(invalidage e1)
      {
          System.out.println(e1.getMessage());
      }
  }
}

class licence{
    public static void main(String args[]){
      Scanner t=new Scanner(System.in);
      System.out.println("Enter lno,name");
      int lno=t.nextInt();
      String nm=t.next();
      System.out.println("Enter address and age");
      String add=t.next();
      int age=t.nextInt();
      driver t5=new driver(lno,nm,add,age);
      t5.check();
     }
}