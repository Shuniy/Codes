#include <iostream>
#include <algorithm>

using namespace std;

void circularSubArray(int a[90], int n)
{
    int b[n];
    for (int i = 0; i < n; i++)
    {
        b[i] = -1 * a[i];
    }
    int negativeSum = 0;
    for (int i = 0; i < n; i++)
    {
        negativeSum += b[i];
    }
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += a[i];
    }
    int circularSum = 0;
    circularSum = sum - (- negativeSum);
    cout << "Circular max sum is : " << circularSum;
}

int main()
{
    int a[] = {10, -3, -4, 7, 6, 5, -4, -1};
    int n = sizeof(a)/sizeof(a[0]);
    circularSubArray(a, n);
    return 0;
}