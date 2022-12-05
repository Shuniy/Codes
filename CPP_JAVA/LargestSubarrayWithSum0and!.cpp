#include<bits/stdc++.h>
using namespace std;

indSubArray(int arr[], int n)
{
    int sum = 0;
    int maxsize = -1, startindex;

    for (int i = 0; i < n-1; i++)
    {
        sum = (arr[i] == 0)? -1 : 1;

        for (int j = i+1; j < n; j++)
        {
            (arr[j] == 0)? (sum += -1): (sum += 1);

            if (sum == 0 && maxsize < j-i+1)
            {
                maxsize = j - i + 1;
                startindex = i;
            }
        }
    }
    if (maxsize == -1)
        cout << "No such subarray";
    else
        cout << startindex << " to " << startindex + maxsize - 1;

    return maxsize;
}

int main()
{
    int arr[] = {1, 0, 0, 1, 0, 1, 1};
    int size = sizeof(arr)/sizeof(arr[0]);

    findSubArray(arr, size);
    return 0;
}