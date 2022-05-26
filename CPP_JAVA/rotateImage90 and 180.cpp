#include <iostream>
#include <algorithm>

using namespace std;

//If rotate 90 degree anticlockwise
//trenaspose and reverse all columns
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
            temp = m[j][i];
            m[j][i] = m[j - i - 1][i];
            m[j - i - 1][i] = temp;
        }
    }
}

//Rotate by 180 degree i,e rotate matrix 2 times.
//Or we can first find the transpose and then reverse all colums and again transpose and reverse all columns

void rotateMatrix180(int m[][4])
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
            temp = m[j][i];
            m[j][i] = m[j - i - 1][i];
            m[j - i - 1][i] = temp;
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