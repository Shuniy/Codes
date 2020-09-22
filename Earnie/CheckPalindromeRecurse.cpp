#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

bool isPalindromeRecurse(string &S, int s, int e)
{
    if (s == e)
    {
        return true;
    }
    if (S[s] != S[e])
    {
        return false;
    }
    if (s <= e )
    {
        return isPalindromeRecurse(S, s + 1, e - 1);
    }
    return true;
}

bool isPalindrome(string s)
{
    int n = s.length();
    if (n == 0)
    {
        return true;
    }
    return isPalindromeRecurse(s, 0, n - 1);
}

int main()
{
    string s = "peep";
    if (isPalindrome(s))
    {
        cout << "Yes";
    }
    else
    {
        cout << "No";
    }
    return 0;
}