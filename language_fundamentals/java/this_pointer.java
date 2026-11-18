import java.util.Scanner;

public class this_pointer
{
    int l, b, area;

    this_pointer(int l, int b)
    {
        this.l = l;
        this.b = b;
    }

    public void calculate()
    {
        this.area = this.l * this.b;
        System.out.println("Area is : " + area);
    }
    public static void main(String[] args)
    {
        Scanner s = new Scanner(System.in);
        int Length, Breadth;
        System.out.println("Enter the length of a rectangle : ");
        Length = s.nextInt();
        System.out.println("Enter the Breadth of a rectangle : ");
        Breadth = s. nextInt();
        this_pointer A = new this_pointer(Length, Breadth);
        A.calculate();
        s.close();
    }
}