#include <iostream>
#include <algorithm>

using namespace std;

//https://www.techiedelight.com/calculate-sum-elements-sub-matrix-constant-time/
int findSubmatrixSum(int mat[][5], int p, int q, int r, int s)
{
    int sum[5][5];
    sum[0][0] = mat[0][0];
    for (int i = 1; i < 5; i++)
    {
        sum[i][0] = mat[i][0] + sum[i - 1][0];
    }
    for (int j = 1; i < 5; j++)
    {
        sum[0][j] = mat[0][j] + sum[0][j];
    }
    for (int i = 1; i < 5; i++)
    {
        for (int j = 1; j < 5; j++)
        {
            sum[i][j] = mat[i][j] + sum[i - 1][j] + sum[i][j - 1] - sum[i-1][j-1];
        }
    }
    int total = sum[r][s];
    if (q-1 >= 0)
    {
        total -= sum[r][q-1];
    }
    if (p - 1 >= 0)
    {
        total -= sum[p-1][s];
    }
    if (q - 1 && p - 1 >= 0)
    {
        total += sum[p-1][q - 1];
    }
    return total;
    {
        /* code */
    }
    
}

int main()
{
    int mat[M][N] =
        {
            {0, 2, 5, 4, 1},
            {4, 8, 2, 3, 7},
            {6, 3, 4, 6, 2},
            {7, 3, 1, 8, 3},
            {1, 5, 7, 9, 4}};

    int p = 1;
    int q = 1;
    int r = 3;
    int s = 3;
    cout << findSubmatrixSum(mat, p, q, r, s);
    return 0;
}