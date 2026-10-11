import java.util.*;
class armstrong
{
    public static void main(String args[])
    {
        Scanner t=new Scanner(System.in);
        System.out.print("Enter starting range: ");
        int i=t.nextInt();
        System.out.print("Enter ending range: ");
        int j=t.nextInt();
        for(int num=i;num<=j;num++)
        {
            int temp=num;
            int sum=0;
            int digits=0;
            int n=num;
            while(n!=0)
            {
                int digit=n%10;
                sum=sum+(digit*digit*digit);
                n=n/10;
            }
            if(sum==temp)
            {
                System.out.println(num);
            }
        }
    }
}