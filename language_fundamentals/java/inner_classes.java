import java.util.Scanner;

public class inner_classes
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
        inner_classes.Circle c = new inner_classes().new Circle();
        c. show();
        inner_classes.Square s = new inner_classes().new Square();
        s.show();
    }
}