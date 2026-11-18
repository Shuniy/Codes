#include <iostream>
#include <algorithm>

using namespace std;

void myCompare(string x, int y)
{
    string xy = x.append(y);
    string yx = y.append(x);
    return xy.compare(yx) > 0 ? 1 : 0;
}

void printlayout(int a[90], int n)
{
    sort(a, a + n, myCompare);
    for (int i = 0; i < n; i++)
    {
        cout << a[i];
    }
}

int main()
{
    int a[] = {54, 546, 548, 60};
    int n = sizeof(a) / sizeof(a[0]);
    printlayout(a, n);
    return 0;
}