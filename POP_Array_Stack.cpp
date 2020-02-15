#include <iostream>
#include <process.h>
#include <stdlib.h>

using namespace std;

const int size = 50;

int push(int stack[], int &top, int ele)
{
    if (top == size - 1)
    {
        return -1;
    }
    else
    {
        top++;
        stack[top] = ele;
    }
    return 0;
}

int pop(int stack[], int & top, int ele)
{
    int ret;
    if (top == -1)
    {
        return -1;
    }
    else
    {
        ret = stack[top];
        top --;
    }
    return ret;
}

void display(int stack[], int &top)
{
    cout << stack[top] << " <-- " << endl;
    for (int i = top - 1; i >= 0; i--)
    {
        cout << stack[i] << endl;
    }
}

int main()
{
    int stack[size], item, top = -1, res;
    char ch = 'y';
    while (ch == 'y' || ch == 'Y')
    {
        cout << "\nEnter Item for insertion : ";
        cin >> item;
        res = push(stack, top, item);
        if (res == -1)
        {
            cout << "Overflow";
            exit(1);
        }
        cout << "\nThe Stack now is : " << endl;
        display(stack, top);
        cout << "Want to insert more elements (y/n) : ";
        cin >> ch;
    }

    cout << "Now Deletion starts (y/n) : ";
    cin >> ch;
    while (ch == 'y' || ch == 'Y')
    {
        res = pop(stack, top, item);
        if (res == -1)
        {
            cout << "Underflow";
            exit(1);
        }
        cout << "Element deleted is : " << res << endl;
        cout << "\nThe Stack now is : " << endl;
        display(stack, top);
        cout << "Want to insert more elements (y/n) : ";
        cin >> ch;
    }
    return 0;
}