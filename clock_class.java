import java.util.*;
class Clock {
    int hours,minutes,seconds;
   
    Clock(int h, int m, int s)
    {
        hours=h;
        minutes=m;
        seconds=s;
    }

        boolean isValid() 
      {
        if (hours<0 || hours>23) 
       {
            return false;
        }

        if (minutes<0 || minutes>59) 
        {
            return false;
        }

        if (seconds<0 || seconds>59) 
          {
            return false;
        }

        return true;
    }

    void displayAMPM() 
       {
        int h=hours;
        String period;

        if(h>=12)
            {
            period="PM";
        } 
          else 
             {
            period="AM";
        }

        if(h==0) 
        {
            h=12;
        } 
         else if(h>12) 
      {
            h=h-12;
        }

        System.out.printf("Time in AM/PM format: %02d:%02d:%02d %s%n",
                h, minutes, seconds, period);
    }
}

public class clock_class
  {
    public static void main(String[] args) 
{

        Scanner sc=new Scanner(System.in);
        System.out.print("Enter Hours   : ");
        int h=sc.nextInt();
        System.out.print("Enter Minutes : ");
        int m=sc.nextInt();
        System.out.print("Enter Seconds : ");
        int s=sc.nextInt();
        Clock c=new Clock(h, m, s);
        if (c.isValid()) 
         {
            System.out.println("\nValid Time");
            c.displayAMPM();
        }
             else {
            System.out.println("\nInvalid Time");
            System.out.println("Please enter valid hours, minutes and seconds.");
        }
    }
}