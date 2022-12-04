abstract class Person
{
    protected String name;
    protected int age;

    Person (String name, int age)
    {
        this.name = name;
        this.age = age;
    }

    public String getName()
    {
        return this.name;
    }

    public int getAge()
    {
        return this.age;
    }

    abstract void works();
}

class Employee extends Person
{
    private String employeeID;
    private String Department;

    public Employee (String name, int age, String employeeID, String Department)
    {
        super(name, age);
        this.employeeID = employeeID;
        this.Department = Department;
    }

    public String getEmployeeID()
    {
        return employeeID;
    }

    public String getDepartment()
    {
        return Department;
    }

    public void works()
    {
        if (this.employeeID != null)
        {
            System.out.println("Employee currently works here");
        }
        else
        {
            System.out.println("Employee doesn't work here");
        }
    }
}

public class AbstractClass
{
    public static void main(String args[])
    {
        Employee e1 = new Employee("Shubham Kumar", 27, "S1001", "software");
        Employee e2 = new Employee("Shubham Sucks", 29, null, "Lost");
        e1.works();
        e2.works();
    }
}