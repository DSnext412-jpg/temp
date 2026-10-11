abstract class shape
{
 abstract void area(int r, int h);
 abstract void volume(int r, int h);
}
  class cylinder extends shape
{
  void area(int r, int h)
  {
 float ans=2*3.14f*r*r*h;
System.out.println("area of cylinder" +ans);
  }
void volume(int r, int h)
{
 float ans1=3.14f*r*r*h;
 System.out.println("volume of cylinder" +ans1);
}
}

class abstract_class
{
public static void main(String args[])
 {
  shape t;
  cylinder t1=new cylinder();
  t=t1;
  t.area(5,7);
  t.volume(3,2);
  }
}
