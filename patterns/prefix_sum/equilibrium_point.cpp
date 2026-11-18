#include <iostream>
#include <algorithm>

using namespace std;
//Either run two loops
void equilibrium(int a[50], int n)
{
    int leftSum = 0;
    int rightSum = 0;
    for (int i = 0; i < j; i++)
    {
        leftSum += a[i];
        for (int j = i + 1; j < n; j++)
        {
            rightSum += a[j];
        }
        if (leftSum = rightSum)
        {
            cout << i;
        }
    }
}

//O(n)
void equilibriumPoint1(int a[50], int n)
{
    int sum = 0;
    int leftSum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += a[i];
    }
    for (int i = 0; i < n; i++)
    {
        sum -= a[i];
        if (leftSum == sum)
        {
            cout << i << endl;
            break;
        }
        leftSum += a[i];
    }
}

int main()
{
    int a[]= {1,3,5,2,2};
    int n = sizeof(a)/sizeof(a[0]);
    equilibriumPoint(a, n;)
}