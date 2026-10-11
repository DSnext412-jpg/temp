import java.util.*;
class employee
{
    int eid;
    String name;
    float salary;
        void accept()
    {
        Scanner t= new Scanner(System.in);
        System.out.print("Enter Employee ID: ");
        eid = t.nextInt();
        System.out.print("Enter Employee Name: ");
        name = t.next();
        System.out.print("Enter Employee Salary: ");
        salary = t.nextFloat();
    }
       void display()
    {
        System.out.println("Employee ID     : " + eid);
        System.out.println("Employee Name   : " + name);
        System.out.println("Employee Salary : " + salary);
    }
}

class emp
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of employees: ");
        int n = sc.nextInt();
        employee e[] = new employee[n];
        for (int i = 0; i < n; i++)
        {
            System.out.println("\nEnter details of Employee " + (i + 1));

            e[i] = new employee();
            e[i].accept();
        }

        int max = 0;
        for (int i = 1; i < n; i++)
        {
            if (e[i].salary > e[max].salary)
            {
                max = i;
            }
        }
        System.out.println("\nEmployee having Maximum Salary:");
        e[max].display();
    }
}