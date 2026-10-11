import java.util.*;
interface calculate
{
   public void add(int a,int b);
  public void sub(int a,int b);
 
}
class simplecalc implements calculate
{
  public void add(int a,int b)
  {
    int c=a+b;
    System.out.println("addition is"+c);
  }
public void sub(int a,int b)
  {
    int c=a-b;
    System.out.println("substraction is"+c);
  }

}

class calculator
{
    public static void main(String args[])
     {
         Scanner t=new Scanner(System.in);
         System.out.println("Enter two numbers");
         int x=t.nextInt();
          int y=t.nextInt();
         calculate t1;
           simplecalc t2=new simplecalc();
           t1=t2;
         t1.add(x,y);
          t1.sub(x,y);
     }
}