import java.util.Scanner;

public class MethodOverloading
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
        MethodOverloading.area(5, 3);
        MethodOverloading.area(5);
    }
}