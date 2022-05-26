import java.util.Scanner;

class Factorial
{
    public static void main(String args[])
    {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter the Number : ");
        int num = s.nextInt();
        int factorial = fact(num);
        System.out.println("Factorial of entered number is : " + factorial);
        s.close();
    }

    static int fact(int n)
    {
        int output;
        if(n == 1)
        {
            return 1;
        }
        else
        {
            output = n * fact(n-1);
            return output;
        }
    }
}