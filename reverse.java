import java.io.*;
class reverse_case
{
    public static void main(String args[]) throws Exception
    {
        RandomAccessFile f = new RandomAccessFile("abc.txt", "r");
        for(long i=f.length()-1;i>=0;i--)
        {
            f.seek(i);
            char ch=(char) f.read();
            if(ch>='A' && ch<='Z')
            {
                ch=(char)(ch + 32);
            }
            else if(ch>='a' && ch<='z')
            {
                ch=(char)(ch - 32);
            }
            System.out.print(ch);
        }
        f.close();
    }
}
