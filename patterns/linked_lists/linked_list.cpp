#include <iostream>
#include <cstdlib>

using namespace std;

struct node{
    int data;
    node *next;
} *head, *newptr, *ptr, *local;

node *CreateNewNode(int);
void InsertAtBeginning(node *);
void InsertInMiddle(node *, int);
void InsertAtEnd(node *);
void DeleteAtBeginning();
void DeleteInMiddle(int);
void DeleteAtEnd();
void display(node *);

int main()
{
    head = NULL;
    int data;
    string choice1;

    cout<<"Do you want to create a node (Y/N) : ";
    cin >>choice1;

    while (choice1 == "y"|| choice1 == "Y")
    {
        cout<<"\nEnter the integer data : ";
        cin >>data;
        cout<<"Creating a new node !"<<endl;
        newptr = CreateNewNode(data);

        if (newptr != NULL)
        {
            cout<<"Node created successfully !"<<endl;
        }
        else
        {
            cout<<"Can't create node ! Aborting !";
            break;
        }

        cout<<"From where do you want to insert the node (B - Beginning, M - Middle, E - End) : ";
        string choice2;
        cin >>choice2;

        if (choice2 == "B" || choice2 == "b")
        {
            InsertAtBeginning(newptr);
        }
        else if (choice2 == "M" || choice2 == "m")
        {
            cout<<"Enter the position from where to delete : ";
            int pos;
            cin >>pos;
            InsertInMiddle(newptr, pos);
        }
        else if (choice2 == "E" || choice2 == "e")
        {
            InsertAtEnd(newptr);
        }
        else
        {
            cout<<"Invalid input ! ";
        }

        cout<<"Do you want to add more nodes (Y/N) : ";
        cin >>choice1;
        }

        cout<<"Do you want to delete a node (Y/N) : ";
        string choice3;
        cin >>choice3;

        while (choice3 == "y"|| choice3 == "Y")
        {
            cout<<"From where do you want to delete the node (B - Beginning, E - End) : ";
            string choice4;
            cin >>choice4;

            if (choice4 == "B" || choice4 == "b")
            {
                DeleteAtBeginning();
            }
            else if (choice4 == "E" || choice4 == "e")
            {
                DeleteAtEnd();
            }
            else
            {
                cout<<"Wrong input ! Aborting !";
            }

            cout<<"Do you want to delete more nodes : ";
            cin >>choice3;
        }
    return 0;
}


node *CreateNewNode(int Data)
{
    ptr = new node;
    ptr -> data = Data;
    ptr -> next = NULL;
    return ptr;
}

void InsertAtBeginning(node *ptr)
{
    if (head == NULL)
    {
        head = ptr;
    }
    else
    {
        local = new node;
        local = head;
        head = ptr;
        ptr -> next = local;
    }
    display(head);
}

void InsertAtEnd(node *ptr)
{
    if (head == NULL)
    {
        head = ptr;
    }
    else
    {
        local = new node;
        local = head;
        while(local != NULL)
        {
            local -> next = ptr;
            local = ptr;
        }
    }
    display(head);
}

void InsertInMiddle(node *ptr, int pos)
{
    if (pos < 1)
    {
        cout<<"Invalid !! ";
    }
    else
    {
        if (head == NULL)
        {
            head = ptr;
        }
        else
        {
            local = new node;
            local = head;
            while(pos--)
            {
                node *temp;
                temp = new node;
                temp = local;
                local -> next = ptr;
                ptr -> next = temp -> next;
            }

        }
    }
    display(head);
}

void display(node *ptr)
{
    while (ptr != NULL)
    {
        cout<<ptr->data<<" -> ";
        ptr = ptr -> next;
    }
    cout<<"NULL"<<endl;
}

void DeleteAtBeginning()
{
    if (head == NULL)
    {
        cout<<"Underflow !! ";
    }
    else
    {
        ptr = new node;
        ptr = head;
        head = head -> next;
        delete ptr;
    }
    display(head);
}

void DeleteAtEnd()
{
    if (head == NULL)
    {
        cout<<"Underflow !! ";
    }
    else
    {
        ptr = new node;
        ptr = head;
        while(ptr != NULL)
        {
            delete ptr;
        }
    }
    display(head);
}
