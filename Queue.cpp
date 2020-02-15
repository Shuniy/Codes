#include <iostream>
#include <stdlib.h>
#include <process.h>

using namespace std;
const int size = 50;
int queue[size], front = -1, rear = -1;

int insert(int queue[], int ele)
{
    if (rear == size - 1)
    {
        return -1;
    }
    else if (rear == -1)
    {
        front = rear = 0;
        queue[rear] = ele;
    }
    else
    {
        rear++;
        queue[rear] = ele;
    }
    return 0;
}

int remove(int queue[])
{
    int ret;
    if (front == -1)
    {
        return -1;
    }
    else
    {
        ret = queue[front];
        if (front == rear)
        {
            front = rear = -1;
        }
        else
        {
            front++;
        }
    }
    return ret;
}

void display(int queue[], int front, int rear)
{
    if (front == -1)
    {
        return;
    }
    for (int i = front; i < rear; i++)
    {
        cout << queue[i] << " <-- ";
    }
    cout << queue[rear] << endl;
}

int main()
{
    int item, res;
    char ch = 'y';

    system("cls");

    while (ch == 'y' || ch == 'Y')
    {
        cout << "Enter the item for insertion : ";
        cin >> item;
        res = insert(queue, item);
        if (res == -1)
        {
            cout << "Overflow";
            exit(1);
        }
        cout << "Now the queue (Front to rear) is : ";
        display(queue, front, rear);
        cout << endl
             << "Want to insett more element (y/n) : ";
        cin >> ch;
    }

    cout << "Now deletion begins ...";
    ch = 'y';
    while (ch == 'y' || ch == 'Y')
    {
        res = remove(queue);
        if (res == -1)
        {
            cout << "underflow";
            exit(1);
        }
        else
        {
            cout << "Element deleted is : " << res << endl;
            cout << "Now the queue (Front to rear) is : " << endl;
            display(queue, front, rear);
        }
        cout << endl
             << "Want to delete more element (y/n) : ";
        cin >> ch;
    }
    return 0;
}