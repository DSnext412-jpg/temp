import java.io.*;
import java.util.*;
class count
{
  public static void main(String args[])throws Exception
    {
    Scanner t=new Scanner(System.in);
    System.out.println("Enter file name");
    String fname=t.next();
    BufferedReader br=new BufferedReader(new FileReader(fname));
    int c=0,w=0,l=0;
    String str;
    while((str=br.readLine())!=null)
    {
      l++;
      c=c+str.length();
      String []a=str.trim().split("\\s+");
      if(!str.trim().isEmpty())
      {
        w=w+a.length;
      }
}
   System.out.println("lines"+l+"char"+c+"words"+w);
      }

}