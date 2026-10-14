import java.io.*;
class zeronum extends Exception
{
    zeronum(String msg)
     {
    super(msg);
    }
}
class number_is_zero
{
   public static void main(String args[])throws Exception
  {
  int f=0;
   BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    try
     {
  System.out.println("Enter number");
int no=Integer.parseInt(br.readLine());
   if(no==0)
  throw new zeronum("number is zero");
    else
     {
      for(int i=2;i<no;i++)
      {
        if(no%i==0)
        { 
          f=1;
          break;
        }
      }
    if(f==1)
         System.out.println(no+"is not prime");
    else
       System.out.println(no+"is prime");
   }   
   }catch(zeronum e)
    { 
    System.out.println(e.getMessage());
    }
  }
}
