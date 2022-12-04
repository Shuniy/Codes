#include <iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int MatrixChainMultiplication(int a[], int n)
{
    int m[5][5] = {0};
    int s[5][5] = {0};
    int j, min, q, d;
    for (d = 0; d < n - 1; d++)
    {
        for (int i = 1; i < n - d; i++)
        {
            j = i + d;
            min = INT_MAX;
            for (int k = i; k < j - 1; k++)
            {
                q = m[i][k] + m[k + 1][j] + a[i - 1] * a[k] * a[j];
                if  (q < min)
                {
                    min = q;
                    s[i][j] = k;
                }
                m[i][j] = min;
            }
        }
    }
    return m[1][n - 1];
}

int main()
{
    int a[] = {1, 2, 3, 4};
    int n = sizeof(a) / sizeof(a[0]);
    cout << "Minimum number of multiplications is " << MatrixChainMultiplication(a, n);
    return 0;
}