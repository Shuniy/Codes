import java.util.Scanner;

public class InnerClasses
{
    class Circle
    {
        public void show()
        {
            System.out.println("In Inner class Circle");
        }
    }

    class Square
    {
        public void show()
        {
            System.out.println("In inner class Square");
        }
    }

    public static void main (String[] args)
    {
        InnerClasses.Circle c = new InnerClasses().new Circle();
        c. show();
        InnerClasses.Square s = new InnerClasses().new Square();
        s.show();
    }
}