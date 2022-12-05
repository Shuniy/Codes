import java.util.Scanner;

public class LeapYear
{
    public static void main(String args[])
    {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter any year : ");
        int year = s.nextInt();
        s.close();
        boolean Leap = false;
        if (year % 4 == 0)
            if (year % 100 == 0)
                if (year % 400 == 0)
                    Leap = true;
                else
                    Leap = false;
            else
                Leap = true;
        else
            Leap = false;
        if (Leap == true)
            System.out.println(year + " is a leap year.");
        else
            System.out.println(year + " is not a leap year.");
    }
}