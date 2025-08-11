#include <iostream>
#include <algorithm>
#include <random>
#include <cstdlib>
#include <vector>

using namespace std;

void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

void shell_sort(int a[], int n)
{
    int h = 1;
    int i, j;
    while (h < n/3)
    {
        h = 3*h +1;
    }

    while (h >= 1)
    {
        for (i = h; i < n; i++)
        {
            for(j = i; (j >= h) && (a[j - h] > a[i]); j -= h)
            {
                a[j] = a[j - h];
            }
            a[j] = a[i];
        }
        h = h / 3;
    }
}

int main()
{
    cout << "How many random numbers to generate : ";
    int n;
    cin >> n;

    int a[n];
    for (int i = 0; i < n; i++)
    {
        a[i] = rand();
    }
    cout << "Generated numbers are : " << endl;
    for (int i = 0; i < n; i++)
        cout << a[i] << " ";

    shell_sort(a, n);

    cout << endl
         << "Sorted numbers are : " << endl;
    for (int i = 0; i < n; i++)
        cout << a[i] << " ";

    return 0;
}