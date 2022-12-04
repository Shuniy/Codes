import java.util.Scanner;

public class Fibonacci
{
    public static void main(String args[])
    {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter the limit of fibonacci series : ");
        int num = s.nextInt();
        System.out.println("Fibonacci series upto entered limt is : ");
        fib(num);
        s.close();
    }
    static void fib(int n)
    {
        int a = 0;
        int b = 1;
        System.out.print(a + " " + b);
        while(n -2 > 0)
        {
            int c = a + b;
            a = b;
            b = c;
            System.out.print(" " + c);
            n--;
        }
    }
}