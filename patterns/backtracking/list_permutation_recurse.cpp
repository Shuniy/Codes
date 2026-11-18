#include <iostream>
#include <algorithm>
#include <bits/stdc++.h>
#include <string>

using namespace std;

void permutations(string &S, int s, int e)
{
    if(s == e)
    {
        cout << S << " ";
    }
    else
    {
        for (int i = 1; i <= e; i++)
        {
            swap(S[s], S[i]);
            permutations(S, s + 1, e);
            swap(S[s], S[i]);
        }
    }
}

int main()
{
    string s = "ABC";
    int n = s.length();
    permutations(s, 0, n - 1);
    return 0;
}