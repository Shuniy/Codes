#include <iostream>
#include <bits/stdc++.h>
#include <vector>
#include <algorithm>

using namespace std;

int LinearSearch(int a[], int n, int k)
{
    for (int i = 0; i < n; i++)
    {
        if (a[i] == k)
        {
            return i + 1;
        }
    }
    return -1;
}

int BinarySearch(int a[], int s, int l, int k)
{
    int mid;
    if (l >= 1)
    {
        mid = s + (l - 1)/2;
        if (a[mid] == k)
        return mid;
    }
    if (a[mid] > k)
    {
        return BinarySearch(a, s, mid - 1, k);
    }
    return BinarySearch(a, mid + 1, l, k);
}

int main ()
{
    int a[40], n, k;
    char s;
    
    cout << "Enter the size of the array : ";
    cin >> n;
    cout << "\nDo you want to perform Linear Search(l) or Binary Search(b) : (l/b) : ";
    cin >> s;

    if (s == 'L' || s == 'l')
    {
        cout <<"\nEnter the array elements : ";
        for (int i = 0; i < n; i++)
        {
            cin >>a[i];
        }
        cout << "\nEnter the element you want to find : ";
        cin >> k;
        int result = LinearSearch(a, n, k);
        if (result == -1)
        {
            cout << "\nNot Found ! ";
        }
        else
        {
            cout << "\nFound at position : "<< result;
        }
    }
    else if (s == 'b' || s == 'B')
    {
        cout << "\nEnter sorted array elements : ";
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
        }
        cout << "\nEnter the element you want to find : ";
        cin >> k;
        int result = BinarySearch(a, 1, n, k);
        if (result == -1)
        {
            cout << "\nNot Found ! ";
        }
        else
        {
            cout << "\nFound at position : " << result + 1;
        }
    }
    else
    {
        cout << "Wrong Input !";
        return 0;
    }
}