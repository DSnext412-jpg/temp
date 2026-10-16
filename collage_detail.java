class college
{
    int cno;
    String cnm,cadd;
    void accept(){
            cno=101;
            cnm="kkw";
            cadd="Nashik";
      }
    void disp(){
            System.out.println("College details"+cno+"-"+cnm+"-"+cadd);
     }

}
class dept extends college
 {
       String dnm,dno;
        void accept1()
           {
                 dno="c101";
                 dnm="computer";                
          }
        void show()
        {
              System.out.println("department details"+dno+"-"+dnm);
         }
 }
class collage_detail
{
     public static void main(String args[])
       {
      dept t=new dept();
      t.accept();
      t.disp();
      t.accept1();
     t.show();

       }
 


}
