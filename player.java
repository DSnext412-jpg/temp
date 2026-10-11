import game.*;

public class player
{
         public static void main(String args[])
         {
               Indoor t=new Indoor(); 
                  t.display();
                  Indoor t1=new Indoor("chess","xyz");
                  t1.display(); 
                  Outdoor t2=new Outdoor(); 
                  t2.display();
                  Outdoor t3=new Outdoor("football","messi");
                  t3.display(); 
         }
}


/*
package game;
public class Indoor
{
       String gname,pname;
         public Indoor()
         {
                  gname="carrom";
                  pname="abc";
                  
          }
          public Indoor(String gname, String pname)
          {
                  this.gname= gname;
                  this.pname= pname;
           }
           public void display()
           {
                  System.out.println("Indoor Games");
                  System.out.println("Game:"+gname);
                  System.out.println("Player:"+pname);
            }
}


package game;
public class Outdoor        
{
       String gname,pname;
         public Outdoor()
         {
                  gname="Cricket";
                  pname="Rohit Sharma";
                  
          }
          public Outdoor(String gname, String pname)
          {
                  this.gname= gname;
                  this.pname= pname;
           }
           public void display()
           {
                  System.out.println("Outdoor Games");
                  System.out.println("Game:"+gname);
                  System.out.println("Player:"+pname);
            }
}
*/