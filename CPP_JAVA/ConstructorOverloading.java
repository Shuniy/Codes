import java.util.scanner;

public class ConstructorOverloading
{
    int x, y;
    public ConstructorOverloading()
    {
        this.x = 0;
        this.y = 0;
    }

    public ConstructorOverloading(int x)
    {
        this.x = x;
    }

    public ConstructorOverloading(int x, int y)
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
        ConstructorOverloading a = new ConstructorOverloading();
        a.print();
        ConstructorOverloading b = new ConstructorOverloading(9);
        b.print();
        ConstructorOverloading c = new ConstructorOverloading(8, 9);
        c.print();
    }
}