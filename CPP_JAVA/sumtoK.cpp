#include <iostream>
#include <algorithm>
#include <bits/stdc++.h>

using namespace std;

void sumtoK(int a[60], int n, int targetSum)
{
    unordered_set<int> s;
    for (int i = 0; i < n; i++)
    {
        int temp = sum - a[i];
        if(s.find(temp) != s.end())
        {
            cout << "Pair with given sum is : " << a[i] << " ," << temp;
        }
        s.insert(a[i]);
    }
}

int main()
{
    int a[] = {1, 4, 45, 6, 10, 8};
    int n = sizeof(a)/sizeof(a[0]);
    int targetSum;
    cin >> targetSum;
    sumtoK(a, n, targetSum);
    return 0;
}