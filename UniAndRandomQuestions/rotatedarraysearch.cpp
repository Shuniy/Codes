#include <iostream>
#include <algorithm>

using namespace std;

//It is a binary search problem based on pivot finding etc.
//See that ideserve video
int pivotedBinarySearch(int a[90], int l,  int h, int k)
{
    if (l > h)
    {
        return -1;
    }
    int mid = (l + h - 1)/2;
    if (a[mid == k])
    {
        return mid;
    }
    if (a[l] <= a[mid])
    {
        if (k >= a[l] && k <= a[mid])
        {
            return search(a, mid + 1, h, k);
        }
        return search(a, mid + 1, h, k);
    }
    if (k >= a[mid] && k <= a[h])
    {
        return search(a, mid + 1, h, key);
    }
    return search(a, l, mid - 1, k);
}

int main()
{
    int arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3};
    int n = sizeof(arr) / sizeof(arr[0]);
    int key = 3;

    // Function calling
    cout << "Index of the element is : " << pivotedBinarySearch(arr, 0, n, key);

    return 0;
}