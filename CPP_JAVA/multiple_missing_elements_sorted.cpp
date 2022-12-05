#include <iostream>

// array is : 6,7,8,9,11,12,15,16,17,18,19
using namespace std;

void missing_elements(int a[], int size)
{
    int diff, l, h;
    l = a[0];
    h = a[size - 1];
    diff = l - 0;
    for (int i = 0; i < size; i++)
    {
        if (a[i] - i != diff)
        {
            while (diff < a[i] - i)
            {
                cout << "Missing element is : " << i + diff << endl;
                diff ++;
            }
        }
    }
}

int main()
{
    int a[] = {6,7,8,9,11,15,16,17, 18, 19};
    int size = sizeof(a) / sizeof(a[0]);
    missing_elements(a, size);
    return 0;
}