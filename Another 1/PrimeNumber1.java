import java.util.Scanner;

public class PrimeNumber1
{
    public static void main(String args[])
    {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter number of prime numbers you want : ");
        int num = s.nextInt();
        s.close();
        int count, i = 1, j = 1;
        while (num > 0)
        {
            j = 1;
            count = 0;
            while (j <= i)
            {
                if (i % j == 0)
                    count++;
                j++;
            }
            if (count == 2)
            {
                System.out.print(" " + i);
                num--;
            }
            i++;
        }
    }
}