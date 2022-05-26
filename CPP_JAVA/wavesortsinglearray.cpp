#include <iostream>
#include <algorithm>

using namespace std;

//Either sort the array and swap alternate positions

// All even positioned elements are greater than the adjacent odd elements if not then swap
//No need to worry about odd positioned elements
void wavesort(int a[90], int n)
{
    for (int i = 0; i < n; i += 2)
    {
        if (i > 0 && a[i - 1] > a[i])
        {
            swap(a[i], a[i - 1]);
        }
        if (i < n - 1 && a[i] < a[i + 1])
        {
            swap(a[i], a[i + 1]);
        }
    }
    for (int i = 0; i < n; i++)
    {
        cout << a[i] << " ";
    }
}

int main()
{
    int a[] = {2,3,1,5,7,8,4,6};
    int n = sizeof(a)/sizeof(a[0]);
    wavesort(a, n);
    return 0;
}