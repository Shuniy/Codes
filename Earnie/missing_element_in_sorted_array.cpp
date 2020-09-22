#include <iostream>

// array is : 6,7,8,9,10,11,13,14,15,16,17
using namespace std;

void missing_element1(int a[], int size)
{
    int diff, l, h;
    l = a[0];
    h = a[size - 1];
    diff = l -0;
    for (int i = 0; i < size; i++)
    {
        if (a[i] - i != diff)
        {
            cout << "Missing element is : " << i + diff;
            break;
        }
    }
}

void missing_element2(int arr[], int size)
{
    int mid, l, h;
    l = 0;
    h = size - 1;
    while ((h - l) > 1)
    {
        mid = (l + h) / 2;
        if ((arr[l] - l) != (arr[mid] - mid))
        {
            h = mid;
        }
        else if ((arr[h] - h) != (arr[mid] - mid))
        {
            l = mid;
        }
    }
    cout << "Missing element is : " << arr[mid] + 1;
}

int main ()
{
    int a[] = { 6,
                7,
                8,
                9,
                10,
                11,
                13,
                14,
                15,
                16,
                17 };

    int diff, l, h, n;

    int size = sizeof(a)/sizeof(a[0]);
    missing_element2(a, size);
    return 0;
}