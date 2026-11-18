#include <bits/stdc++.h>
using namespace std;

struct Node
{
    int key;
    Node *next;
};

Node *newNode(int key)
{
    Node *temp = new Node;
    temp->key = key;
    temp->next = NULL;
    return temp;
}

void printList(Node *head)
{
    while (head != NULL)
    {
        cout << head->key << " ";
        head = head->next;
    }
    cout << endl;
}

void detectLoop(Node *head)
{
    Node *slowPtr, *fastPtr;

    slowPtr = head;
    fastPtr = head;

    while (slowPtr != NULL && fastPtr != NULL && fastPtr->next != NULL)
    {
        slowPtr = slowPtr->next;
        fastPtr = fastPtr->next->next;
        if (slowPtr == fastPtr)
        {
            cout << ("Loop Detected ");
            break;
        }
    }

    slowPtr = head;

    while (slowPtr != NULL && fastPtr != NULL && fastPtr->next != NULL)
    {
        slowPtr = slowPtr->next;
        fastPtr = fastPtr->next;
        if (slowPtr == fastPtr)
        {
            cout << ("Loop Detected at : ");
            cout << slowPtr->key;
            exit(0);
        }
    }
}

int main()
{
    Node *head = newNode(1);
    head->next = newNode(2);
    head->next->next = newNode(3);
    head->next->next->next = newNode(4);
    head->next->next->next->next = newNode(5);

    head->next->next->next->next->next = head->next->next;
    detectLoop(head);
    return 0;
}
