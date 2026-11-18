#include <iostream>
#include <algorithm>
#include <bits/stdc++.h>

#define EPS 1e-9

using namespace std;

//O(n)time and space
void product(int a[60], int n)
{
    int l[n];
    int r[n];
    l[0] = 1;
    r[n - 1] = 1;
    for (int i = 1; i < n; i++)
    {
        l[i] = a[i - 1] * l[i - 1];
    }
    for (int i = 0; i < n; i++)
    {
        cout << r[i] << " ";
    }
    cout << endl;
    for (int i = n - 2; i >= 0; i--)
    {
        r[i] = a[i + 1] * r[i + 1];
    }
    for (int i = 0; i < n; i++)
    {
        cout << r[i] << " ";
    }
    cout << endl;
    for (int i = 0; i < n; i++)
    {
        a[i] = l[i] * r[i];
    }
    for (int i = 0; i < n; i++)
    {
        cout << a[i] << " ";
    }
    cout << endl;
}

//O(n)time and O(1) space
/*
x = a * b * c * d
log(x) = log(a * b * c * d)
log(x) = log(a) + log(b) + log(c) + log(d)
x = antilog(log(a) + log(b) + log(c) + log(d))
*/
void product(int a[90], int n)
{
    long double sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += (long double)log10(a[i]);
    }
    for (int i = 0; i < n; i++)
    {
        cout << (int)(EPS + pow((long double)10, sum - log10(a[i]))) << " ";
    }
}

int main()
{
    int a[] = {1, 2, 3, 4, 5};
    int n = sizeof(a)/sizeof(a[0]);
    product(a, n);
    return 0;
}