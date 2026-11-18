#include <iostream>
#include <memory>
#include <vector>
#include <sstream>
#include <string>

using std::cout;
using std::endl;
using std::cin;
using std::string;
using std::getline;

class Person {

};

struct User {
    string name;
    int age;
};

void celebrateBirthday(User& user)
{
    user.age++;
}

void printUser(const User& user)
{
    std::cout << user.name << " is "
              << user.age << " years old.\n";
}

User* findAdult(User* user)
{
    // result->age means *(user).age
    if (user != nullptr && user->age >= 18)
    {
        return user;
    }

    return nullptr;
}

void incrementByReference(int& value)
{
    value++;
};

void incrementByPointer(int* value)
{
    (*value)++;
};

void incrementByValue(int value)
{
    value++;
};

int main(int argc, char const *argv[])
{
    int number{10};
    int& numberRef = number;
    cout << "Number: " << number << endl;
    cout << "Number reference: " << numberRef << endl;
    cout << "Number address: " << &number << endl;
    cout << "Number reference address: " << &numberRef << endl;
    numberRef = 20;
    cout << "Number: " << number << endl;
    int* numberPtr = &number;
    cout << "Number pointer address: " << &numberPtr << endl;
    cout << "Number pointer value: " << *numberPtr << endl;
    *numberPtr = 30;
    cout << "Number: " << number << endl;
    incrementByReference(number);
    cout << "Number after incrementByReference: " << number << endl;
    incrementByPointer(&number);
    cout << "Number after incrementByPointer: " << number << endl;
    incrementByValue(number);
    cout << "Number after incrementByValue: " << number << endl;

    const int* constNumberPtr = &number;
    cout << "Const number pointer: " << constNumberPtr << endl;
    // *constNumberPtr = 40; // Error: cannot modify value through const pointer
    cout << "Const number pointer value: " << *constNumberPtr << endl;
    int* const constPtrToNumber = &number;
    cout << "Const pointer to number: " << constPtrToNumber << endl;
    *constPtrToNumber = 50; // Allowed: can modify value through const pointer
    cout << "Const pointer to number value: " << *constPtrToNumber << endl;
    // constPtrToNumber = &numberRef; // Error: cannot change address of const pointer
    // const int* const constPtrToConstNumber = &number; // Error: cannot change address of const pointer and cannot modify value through const pointer

    int* pointer{new int{100}};
    cout << "Pointer address: " << pointer << endl;
    cout << "Pointer value: " << *pointer << endl;
    // memory leak if not deleted the dynamically allocated pointer
    delete pointer;
    // dangling pointer, if deleted, but pointer pointing to the deleted memory
    pointer = nullptr;

    int numbers[]{10, 20, 30, 40};
    cout << "Numbers: ";
    for (int i = 0; i < 4; i++)
    {
        cout << numbers[i] << " ";
    }
    cout << endl;

    cout << "Numbers address: " << &numbers << endl;
    cout << "Numbers[0] address: " << &numbers[0] << endl;
    cout << "Numbers[1] address: " << &numbers[1] << endl;
    cout << "Numbers[2] address: " << &numbers[2] << endl;
    cout << "Numbers[3] address: " << &numbers[3] << endl;

    int* numbersPtr = numbers;
    cout << "Numbers pointer address: " << &numbersPtr << endl;
    cout << "Numbers pointer value: " << *numbersPtr << endl;
    for (int i = 0; i < 4; i++)
    {
        cout << *(numbersPtr + i) << " ";
    }
    cout << endl;
    // instead of numbers and pointers use vectors
    std::vector<int> numbersVec{10, 20, 30, 40};
    cout << "Numbers vector: ";
    for (int i = 0; i < numbersVec.size(); i++)
    {
        cout << numbersVec[i] << " ";
    }
    cout << endl;

    // reference is another name for the existing object, a reference must exist
    // ownership
    // Widget* widget{new Widget{}};
    // who should delete the widget?
    // the owner of the widget should delete it, but if the owner is not clear,
    // then it can lead to memory leak or dangling pointer
    // The current function?
    // another object?
    // caller?
    // a container?
    // nobody?
    // Modern C++ expresses ownership explicitly:
    std::unique_ptr<Person> person{std::make_unique<Person>()};
    // this means, if person is destroyed, then the Person object will be destroyed too, and the memory will be freed

    User user{"Alice", 25};
    celebrateBirthday(user);
    printUser(user);

    User* result{findAdult(&user)};
    if (result != nullptr)
    {
        cout << result->name << " is an adult." << endl;
    }
    else
    {
        cout << user.name << " is not an adult." << endl;
    }

    return 0;
}
