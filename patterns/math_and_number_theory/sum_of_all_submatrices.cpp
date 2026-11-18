#include <iostream>
#include <algorithm>

using namespace std;
/*
For each element of the matrix, let us try to find the number of sub-matrices,
the element will lie in.
This can be done in O(1) time. Let us suppose the index of an element be (X, Y)
in 0 based indexing, then the number of submatrices (Sx, y) for this element
 will be in can be given by the formula Sx, y = (X + 1) * (Y + 1) * (N – X) * (N – Y) . 
This formula works, because we just have to choose two different positions on 
the matrix that will create a submatrix that envelopes the element. Thus, for each 
 element, ‘sum’ can be updated as sum += (Sx, y) * Arrx, y.

 O(n^2)
*/
int matrixSum(int a[][3])
{
    int sum = 0;
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; i < n; j++)
        {
            int topLeft = (i + 1) * (j + 1);
            int bottomRight = (3 - i) * (3 - j);
            sum += topLeft * bottomRight * a[i][j];
        }
    }
    return sum;
}

//Generate all submatrices and calculate sum O(n ^ 6)

int main()
{
    int arr[][n] = {{1, 1, 1},
                    {1, 1, 1},
                    {1, 1, 1}};

    cout << matrixSum(arr);

    return 0;
}