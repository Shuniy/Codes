#include <iostream>
#include <stdlib.h>
#include <process.h>

using namespace std;

const int size = 50;

int cqueue[size], front = -1, rear = -1;

int insert_in_cq(int cqueue[], int ele)
{
    if ((front == 0 && rear == size -1) || (front == rear + 1))
    {
        return -1;
    }
    else if (rear == -1)
    {
        front = rear = 0;
    }
    else if (rear == size -1)
    {
        rear = 0;
    }
    else
    {
        cqueue[rear] = ele;
    }
    return 0;
}

void display (int cqueue[], int front, int rear)
{
    int i = 0;
    cout << "Circular queue is : " << endl;
    cout << "(Front shown as >>>, rear is shown as <<< and free space as - )" <<endl;
    if (front == -1)
    {
        return;
    }
    if (rear >= front)
    {
        for (int i = 0; i < front; i++)
        {
            cout << " - ";
        }
        cout << " >>> ";
        for (int i = 0; i < rear; i++)
        {
            cout << cqueue[i] << " <- ";
        }
        cout << cqueue[rear] << " <<< " << endl;
    }
    else
    {
        for (int i = 0; i < rear; i++)
        {
            cout << cqueue[i] << " <- ";
        }
        cout << cqueue[rear] << " <<< ";
        for (int i = 0; i < front; i++)
        {
            cout << " - ";
        }
        cout << " >>> ";
        for (int i = 0; i < size; i++)
        {
            cout << cqueue[i] << " <- ";
        }
        cout << " Wrap around " << endl;
    }
}

int del_in_cq (int cqueue[])
{
    int ret;
    if (front == -1)
    {
        return -1;
    }
    else
    {
        ret = cqueue[front];
        if (front == rear)
        {
            front = rear = -1;
        }
        else if (front == size - 1)
        {
            front = 0;
        }
        else
        {
            front ++;
        }
    }
    return ret;
}

int main ()
{
    int item, res, ch;
    do
    {
        cout << "    Circular Queue Menu " << endl;
        cout << "  1. Insert" << endl;
        cout << "  2. Delete" << endl;
        cout << "  3. Display" << endl;
        cout << "  4. Exit" << endl;
        cout << "Enter you choice (1 - 4) : ";
        cin >>  ch;
        switch (ch)
        {
        case 1: cout << "Enter item of insertion : ";
                cin >> item;
                res = insert_in_cq(cqueue, item);
                if (res == -1)
                {
                    cout << "Overflow";
                }
                else
                {
                    cout << "Now the circular queue is : " << endl;
                    display(cqueue, front, rear);
                }
            break;
        case 2:
            item = del_in_cq(cqueue);
            if (res == -1)
            {
                cout << "Underflow";
            }
            else
            {
                cout << "Item deleted in the circular queue is : " << item << endl;
                display(cqueue, front, rear);
            }
            break;
        case 3:
            display(cqueue, front, rear);
            break;
        case 4:
            break;
        default: cout << "Valid choices are only 1 - 4 only" << endl;
            break;
        }
    } while (ch !=4);
    return 0;
}