import java.util.scanner;

public class constructor_overloading
{
    int x, y;
    public constructor_overloading()
    {
        this.x = 0;
        this.y = 0;
    }

    public constructor_overloading(int x)
    {
        this.x = x;
    }

    public constructor_overloading(int x, int y)
    {
        this.x = x;
        this.y = y;
    }

    public void print()
    {
        System.out.println("X = " + x + " and Y = " + y);
    }
    
    public static void main(String[] args)
    {
        constructor_overloading a = new constructor_overloading();
        a.print();
        constructor_overloading b = new constructor_overloading(9);
        b.print();
        constructor_overloading c = new constructor_overloading(8, 9);
        c.print();
    }
}