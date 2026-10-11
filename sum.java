import java.util.*;
class sum
{
  public static void main(String args[]){
    int sum=0;
    Scanner t =new Scanner (System.in);
    System.out.println("Enter size of array");
    int n=t.nextInt();
    int []a=new int[n];
    for(int i=0;i<n;i++)  
    {
      a[i]=t.nextInt();
      sum=sum+a[i];
    } 
  System.out.println("sum of array elements"+sum);
  Arrays.sort(a);
  System.out.println("sorted element is");
  for(int i=0;i<n;i++)
  {
    System.out.println(a[i]);
    }
  }
}