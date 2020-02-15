#include <iostream>
#include <process.h>

using namespace std;

struct node
{
    int data;
    node * next;
}*front, *newptr, *temp, *ptr, *rear;

node * create_new_node(int n)
{
    ptr = new node;
    ptr -> data = n;
    ptr -> next = NULL;
    return ptr;
}

void insert (node * np)
{
    if (front == NULL)
    {
        front = rear = np;
    }
    else
    {
        rear -> next = np;
        rear = np;
    }
}

void delnode ()
{
    if (front == NULL)
    {
        cout << "Underflow";
        exit(1);
    }
    else
    {
        ptr = front;
        front = front -> next;
        delete ptr;
    }
}

void display (node * np)
{
    while (np != NULL)
    {
        cout << np -> data << " --> ";
        np = np -> next;
    }
    cout << endl;
}

int main ()
{
    front = rear = NULL;
    int data;
    char ch = 'y';
    while (ch == 'y' || ch == 'Y')
    {
        cout << "Enter data for the new node : ";
        cin >> data;
        newptr = create_new_node(data);
        if (newptr == NULL)
        {
            cout << endl << "Cannot create new node ";
            exit(1);
        }
        insert(newptr);
        cout << "Press y to enter more nodes, N to exit : ";
        cin >> ch;
    }
    system("cls");
    do
    {
        cout << endl << "The linked queue now is (front to rear) : ";
        display(front);
        cout << "Want to delete first node (y/n) : ";
        cin >> ch;
        if (ch == 'y' || ch == 'Y')
        {
            delnode();
        }
    } while (ch == 'y' || ch == 'Y');
    return 0;
}
