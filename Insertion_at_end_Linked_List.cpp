#include <iostream>

using namespace std;

struct node
{
    int data;
    node *next;
} * head, *ptr, *newptr, *temp;

node *create_new_node(int k)
{
    ptr = new node;
    ptr->data = k;
    ptr->next = NULL;
    return ptr;
}

void insert_at_end(node *np)
{
    if (head == NULL)
    {
        head = np;
    }
    else
    {
        temp = head;
        while (temp -> next != NULL)
        {
            temp = temp -> next;
        }
        temp -> next = np;
    }
}

void display(node *np)
{
    while (np != NULL)
    {
        cout << np->data << " --> ";
        np = np->next;
    }
    cout << "!!!\n";
}

int main()
{
    head = NULL;
    int info;
    char ch = 'y';

    while (ch == 'y' || ch == 'Y')
    {
        cout << "\n Enter the data for new node : ";
        cin >> info;

        cout << "Creating new node ! ";

        newptr = create_new_node(info);

        if (newptr != NULL)
        {
            cout << "Node created ! ";
        }
        else
        {
            cout << "Cannot create node ! ";
            exit(1);
        }

        cout << "Now inserting node at end ! ";
        insert_at_end(newptr);

        cout << "Now the linked list is : ";
        display(head);

        cout << "Press Y to enter more nodes at beginning else N to exit : ";
        cin >> ch;
    }
    return 0;
}