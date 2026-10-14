interface ProductDetails 
{
    void display();
}
class Product implements ProductDetails {

    int pid;
    String pname;
    double pcost;
    int pquantity;
    static int objectCount=0;

    Product() {
        prid=0;
        pname="Unknown";
        pcost=0.0;
        pquantity=0;
        objectCount++;
    }

    Product(int id, String name, double cost, int quantity) {
        pid=id;
        pname=name;
        pcost=cost;
        pquantity=quantity;
        objectCount++;
    }

    public void display() {
        System.out.println("Product ID :"+pid);
        System.out.println("Product Name:"+pname);
        System.out.println("Product Cost:"+pcost);
        System.out.println("Product Quantity:"+pquantity);
    }
    static void displayObjectCount() {
        System.out.println("Total Objects Created : " + objectCount);
    }
}

public class interface_product
 {
    public static void main(String[] args)
 {
        Product p1=new Product();
        Product p2=new Product(101,"Laptop",55000,2);
        Product p3=new Product(102,"Mouse",800,5);
        Product p4=new Product(103,"Keyboard",1500,3);
        p1.display();
        p2.display();
        p3.display();
        p4.display();
        Product.displayObjectCount();
    }
}
