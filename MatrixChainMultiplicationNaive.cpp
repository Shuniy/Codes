#include <iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int MatrixChainMultiplication(int a[], int i, int j)
{
    int k, count, min;
    min = INT_MAX;
    if (i == j)
    {
        return 0;
    }
    else
    {
        for (k = i; k < j; k++)
        {
            count = MatrixChainMultiplication(a, i, k) + MatrixChainMultiplication(a, k + 1, j) + a[i-1] * a[k] * a[j];
        }
        if (count < min)
        {
            min = count;
        }
    }
    return min;
}

int main()
{
    int a[] = {1, 2, 3, 4, 3};
    int n = sizeof(a) / sizeof(a[0]);
    cout << "Minimum number of multiplications is " << MatrixChainMultiplication(a, 1, n - 1);
    return 0;
}