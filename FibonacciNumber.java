import java.util.Scanner;
import java.util.scanner;

public class FibonacciNumber
{
    public static void main(String args[])
    {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter the position of the fibonacci number : ");
        int num = s.nextInt();
        int result = fib(num);
        System.out.println("Number at position " + num + " is : ");
        System.out.print(result);
        s.close();
    }
    static int fib(int n)
    {
        if (n == 0)
            return 0;
        if (n == 1)
            return 1;
        int Output1 = fib(n-1);
        int output2 = fib(n-2);
        return Output1 + output2;
    } 
}