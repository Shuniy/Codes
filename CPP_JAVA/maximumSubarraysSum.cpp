#include <iostream>
#include <climits>
#include <algorithm>

using namespace std;
//Naive Method is to use two pointers and update sum and check with max sum

//Kadane's Algorithm
int maxSubarray1(int a[90], int n)
{
    int currSum = 0;
    int globalSum = 0;
    for (int i = 0; i < n; i++)
    {
        currSum  = max(currSum, currSum + a[i]);
        if (currSum > globalSum)
        {
            globalSum = currSum;
        }
    }
    return globalSum;
}

//Using Divide and Conquer will take O(nlogn)
int maxCrossingSum(int arr[70], intt l, int m, int h)
{
    int sum = 0;
    int leftSum = INT_MIN;
    for (int i = m; i >= 1; i --)
    {
        sum = sum + arr[i];
        if (sum > leftSum)
        {
            leftSum = sum;
        }
    }
    int sum = 0;
    int rightSum = INT_MIN;
    for (int i = m + 1; i <= h; i ++)
    {
        sum = sum + arr[i];
        if (sum > rightSum)
        {
            rightSum = sum;
        }
    }
    return leftSum + rightSum;
}

int maxSubarray(int arr[700], int l, int h)
{
    if (l == h)
    {
        return arr[l];
    }
    else
    {
        int m = (l + h)/2;
        return max(maxSubarray(arr, l , m), maxSubarray(arr, m +1, h), maxCrossingSum(arr, l, m , h));
    }
}

int main()
{
    int a[] = {1,-2,3,-4,5,6,-7,-8,9};
    int n = sizeof(a)/sizeof(a[0]);
    int max = maxSubarray(a, n);
    cout << "Maximum sum is : " << max;
    return 0;
}