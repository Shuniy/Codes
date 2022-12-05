#include <iostream>

using namespace std;

struct node
{
    int data;
    node *next;
} * head, *ptr, *newptr, *temp, *temp1;

node *create_new_node(int k)
{
    ptr = new node;
    ptr->data = k;
    ptr->next = NULL;
    return ptr;
}

void insert_at_position(node *np, int p)
{
    if (head == NULL)
    {
        head = np;
    }
    else if (p == 1)
    {
        temp = head;
        np->next = temp;
        head = np;
    }
    else
    {
        temp = head;
        while (p--)
        {
            temp = temp->next;
        }
        temp1 = temp;
        temp->next = np;
        np->next = temp1->next;
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

        int p;
        cout << "Enter the valid position you want to enter the node in a linked list : ";
        cin >> p;

        if (p > 1)
        {
            cout <<"Enter one more node !";
            cout << "\n Enter the data for second node : ";
            cin >> info;

            cout << "Creating new node ! ";

            temp1 = create_new_node(info);

            if (temp1 != NULL)
            {
                cout << "Node created ! ";
            }
            else
            {
                cout << "Cannot create node ! ";
                exit(1);
            }
            insert_at_position(temp1, 1);
        }
        cout << "Now inserting node at position ! ";
        insert_at_position(newptr, p);

        cout << "Now the linked list is : ";
        display(head);

        cout << "Press Y to enter more nodes at beginning else N to exit : ";
        cin >> ch;
    }
    return 0;
}