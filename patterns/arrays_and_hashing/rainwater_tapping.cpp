#include <iostream>
#include <algorithm>

using namespace std;

//In O(n^2) you find water at every node and highest building at its left and right

//O(n)
int findWater(int a[67], int n)
{
    int left[n];
    int right[n];
    int water = 0;
    left[0] = a[0];
    for (int i = 1; i < n; i++)
    {
        left[i] = max[left[i -1], left[i]];
    }
    right[n -1] = a[n-1];
    for (int i = n - 2; i >= 0; i--)
    {
        right[i] = max[right[i + 1], right[i]];
    }
    for (int i = 0; i < n; i++)
    {
        water += min(left[i], right[i]) - a[i];
    }
    return water;
}

int main()
{
    int arr[] = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    int n = sizeof(arr) / sizeof(arr[0]);
    cout << "Maximum water that can be accumulated is "
         << findWater(arr, n);
    return 0;
}