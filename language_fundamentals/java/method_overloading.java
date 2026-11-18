import java.util.Scanner;

public class method_overloading
{
    public static void area (int l, int b)
    {
        System.out.println("Area is : " + l * b);
    }

    public static void area(int s)
    {
        System.out.println("Area is : " + s * s);
    }

    public static void main(String[] args) 
    {
        method_overloading.area(5, 3);
        method_overloading.area(5);
    }
}