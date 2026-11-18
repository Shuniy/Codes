#include <iostream>
#include <stdio.h>

using namespace std;

//Naive Method O(n^3)
void subarray1(int *a, int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = i; j < n; j++)
        {
            for (int k = i; k <= j; k++)
            {
                cout << a[k] << " ";
            }
            cout << endl;
        }
    }
}

//Using Recursion
void subarray2(int a[70], int start, int end)
{
    int n = sizeof(a)/sizeof(a[0]);
    if (end == n)
    {
        return;
    }
    else if (start > end)
    {
        subarray2(a, 0, end + 1);
    }
    else
    {
        cout << "[";
        for (int i = start; i < end; i++)
        {
            cout << a[i] << "  ,";
        }
        cout << a[end] << "]" << endl;
        subarray2(a, start + 1, end);
    }
    return;
}

int main()
{
    int a[] = {1,2,3,4};
    int n = sizeof(a)/sizeof(a[0]);
    subarray1(a, n);
    subarray2(a, 0, 0);
    return 0;
}