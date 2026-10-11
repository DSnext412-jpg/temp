import strop.*;
import java.util.*;
class con_comp
{
      public static void main(String args[])
        {
        Scanner t=new Scanner(System.in);
        System.out.println("Enter first string");
        String s1=t.next();
	System.out.println("Enter second string");
        String s2=t.next();

	con t2=new con();
        t2.concat1(s1,s2);

        comp t3=new comp();
        t3.comp1(s1,s2);
      }
}

/*
package strop;
public class con
{
    public void concat1(String s1,String s2)
        {
                String s3=s1+s2;
                System.out.println("concatinetd string is"+s3);
        }

}


package strop;
public class comp
{
    public void comp1(String s1,String s2)
        {
               int z=s1.compareTo(s2);
                   if(z==0)
                       System.out.println("Strings are equal");
                  else
                        System.out.println("strings are not equal");           
      
       }
}
*/