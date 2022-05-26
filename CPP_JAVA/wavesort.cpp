#include <iostream>
#include <algorithm>

using namespace std;

//start with the rightmost element
//decrease i then if i, j =S= n- 1; wave = 1
void sortInWave(int a[][90], int n)
{
    int wave = 1;

    int i;
    int j = n - 1;
    wave = 1;
    while (j > 0)
    {
        if (wave == 1)
        {
            for (i = 0; i < m; i++)
            {
                cout << a[i][j] << " ";
            }
            wave = 0;
            j--;
        }
        else
        {
            for (i = m - 1; i >= 0; i--)
            {
                cout << a[i][j] << " ";
            }
            wave = 1;
            j--;
        }
    }
}

int main()
{
    int arr[] = {10, 90, 49, 2, 1, 5, 23};
    int n = sizeof(arr) / sizeof(arr[0]);
    sortInWave(arr, n);
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    return 0;
}