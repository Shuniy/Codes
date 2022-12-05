#include <iostream>
#include <bits/stdc++.h>

using namespace std;

void printLeaders(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        int j;
        for (j = i + 1; j < size; j++)
        {
            if (arr[i] <= arr[j])
                break;
        }
        if (j == size)
            cout << arr[i] << " ";
    }
}

int main()
{
    int Case, n;

    cout << "Enter how many cases you want : ";
    cin >>  Case;

    while (Case)
    {
        cout << "Enter the number of elements of array :";
        cin >> n;

        int a[n];
        
        cout < "Enter elements of array : ";
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
        }
    }
    
}