#include <iostream>
#include <algorithm>

using namespace std;

//If rotate 90 degree clockwise
//transpose and reverse all rows
void rotateMatrix90(int m[][4])
{
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            if (i != j)
            {
                int temp;
                temp = m[i][j];
                m[i][j] = m[j][i];
                m[j][i] = temp;
            }
        }
    }
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
                int temp;
                temp = m[i][j];
                m[i][j] = m[i][j - i - 1];
                m[i][j - i - 1] = temp;
        }
    }
}

void displayMatrix(int m[][4])
{
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            cout << m[i][j] << " ";
        }
        cout << endl;
    }
}

int main()
{
    int mat[N][N] =
        {
            {1, 2, 3, 4},
            {5, 6, 7, 8},
            {9, 10, 11, 12},
            {13, 14, 15, 16}};
    rotateMAtrix(mat);
    displayMatrix(mat);
    return 0;
}