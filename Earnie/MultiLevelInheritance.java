import javax.smartcardio.Card;

class car
{
    public car()
    {
        System.out.println("Class Car");
    }

    public void VechileType()
    {
        System.out.println("Vechile Type : Car");
    }
}

class Maruti extends car
{
    public Maruti()
    {
        System.out.println("Class Maruti");
    }

    public void brand()
    {
        System.out.println("Brand : Maruti");
    }

    public void speed()
    {
        System.out.println("Max : 90 Kmph");
    }
}

class Maruti800 extends Maruti
{
    public Maruti800()
    {
        System.out.println("Max : 80 Kmph");
    }

    public void speed()
    {
        System.out.println("Max : 80 Kmph");
    }
}

public class MultiLevelInheritance
{
    public static void main(String args[])
    {
        Maruti800 m = new Maruti800();
        m.VechileType();
        m.brand();
        m.speed();
    }
}