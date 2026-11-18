#include <iostream>
#include <algorithm>
#include <bits/stdc++.h>

using namespace std;

void incdescNumbers(int n)
{
    static int value = 1;
    if (((2 * n) - value) == 0)
        {
            return;
        }
        if (value > n)
        {
            cout << ((2 * n) - value);
        }
        else
        {
            cout << value;
        }
        value++;
        incdescNumbers(n);
}

int main()
{
    int n;
    cin >> n;
    incdescNumbers(n);
    return 0;
}