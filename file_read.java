import java.io.*;
class file_read
{
public static void main(String args[]) throws Exception
   {
FileReader f1=new FileReader("abc.txt");
BufferedReader br=new BufferedReader(f1);
String str; 
while((str=br.readLine())!=null)
{
  System.out.print(str.toUpperCase());
}
 f1.close();
}
}