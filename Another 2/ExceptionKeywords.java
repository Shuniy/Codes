import jdk.javadoc.internal.doclets.toolkit.taglets.ThrowsTaglet;

public class ExceptionKeywords
{
    public static void main(String[] args)
    {
        try
        {
            int a = 5;
            int b = 0;
            int c = a / b;
            System.out.println("c");
        }

        catch(ArithmeticException e)
        {
            System.out.println("Cannot divide by zero ! ");
        }
        finally
        {
            System.out.println("In the Finally Block ! ");
        }
        try
        {
            Method();
        }
        catch (Exception e)
        {
            System.out.println(e.toString());
        }
        public void Method() throws IndexOutOfBoundsException
        {
            int a[] = new int[10];
            for (int i = 0; i< 10; i++)
            {
                a[i] = i;
            }
            for (int i = 0; i < 11; i++)
            {
                if (i > 9)
                {
                    throw new IndexOutOfBoundsException();
                }
                System.out.println(a[i]);
            }
        }
    }
}