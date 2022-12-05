import java.util.Scanner;

class Person
{
    protected String name;
    protected int age;

    Person(String name, int age)
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
    public void setAge(int age)
    {
        this.age = age;
    }
}

class Student extends Person
{
    private String Department;
    private int rollNo;

    public Student(String name, int age, String Department, int rollNo)
    {
        super(name, age);
        this.Department = Department;
        this.rollNo = rollNo;
    }
    
    public String getDepartment()
    {
        return this.Department;
    }
    
    public int getRollNo()
    {
        return this.rollNo;
    }

    public void printDetails()
    {
        System.out.println("Name : " + this.name + "\nAge : " + this.age + "\nRollNo. : " + this.rollNo + "\nDepartment : " + this.Department);
    }
}

public class SingleLevelInheritance
{
    public static void main(String[] args)
    {
        Student s = new Student("Shubham Kumar", 20, "CSE", 66);
        System.out.println("Name is : " + s.getName());
        System.out.println("Complete Details : ");
        s.printDetails();
    }
}