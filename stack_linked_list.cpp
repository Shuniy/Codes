#include <iostream>
#include <process.h>
#include <stdlib.h>

using namespace std;

struct node
{
    int data;
    node * next;
}*top, *newptr, *temp, *ptr;

node * create_new_node(int n)
{
    ptr = new node;
    ptr -> data = n;
    ptr -> next = NULL;
    return ptr;
}

void push(node * np)
{
    if (top == NULL)
    {
        top = np;
    }
    else
    {
        temp = top;
        top = np;
        np -> next = temp;
    }
}

void pop()
{
    if (top == NULL)
    {
        cout <<"Underflow ";
        exit(1);
    }
    else
    {
        ptr = top;
        top = top -> next;
        delete ptr;
    }
}

void display(node * np)
{
    while (np != NULL)
    {
        cout << np -> data << " -> ";
        np = np -> next;
    }
    cout << endl;
}

int main()
{
    top = NULL;
    int data;
    char ch = 'y';
    while (ch == 'y' || ch == 'Y')
    {
        cout << "Enter data for the new node : ";
        cin >> data;
        newptr = create_new_node(data);
        if (newptr == NULL)
        {
            cout << "Cannot create node ";
            exit(1);
        }
        push(newptr);
        cout << "Node created ";
        cout << "Want to enter more nodes (y/n) : ";
        cin >> ch;
    }

    do
    {
        cout << "Stack now is : " << endl;
        display(top);
        cout << "Want to pop element (y/n) : ";
        cin >> ch;
        if (ch == 'Y' || ch == 'y')
        {
            pop();
        }
    } while (ch == 'y' || ch == 'Y');
    return 0;
}