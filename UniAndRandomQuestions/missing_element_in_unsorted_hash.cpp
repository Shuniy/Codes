#include <iostream>

// array is : 3,7,4,9,12,6,1,11,2,10
using namespace std;

void missing_elements(int a[], int size)
{
    int max = a[0];
    for (int i = 1; i < size; i++)
    {
        if (a[i] > max)
        {
            max = a[i];
        }
    }
    int min = a[0];
    for (int i = 1; i < size; i++)
    {
        if (a[i] < min)
        {
            min = a[i];
        }
    }
    int b[max];
    for (int i = 0; i < max; i++)
    {
        b[a[i]]++;
    }
    for (int i = min; i <= max; i++)
    {
        if (b[i] == 0)
        {
            cout << "Missing element is : " << i;
        }
    }
}

int main()
{
    int a[] = {3,7,4,9,12,6,1,11,2,10};
    int size = sizeof(a) / sizeof(a[0]);
    missing_elements(a, size);
    return 0;
}