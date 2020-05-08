#include <iostream>
#include <algorithm>
#include <string>
#include <bits/stdc++.h>

using namespace std;

//Either use inbuilt reverse function
//I I am doing it by recursion

void reverseString(string &s, int i = 0)
{
    //Base case
    int n  = s.length();
    if (i == n / 2)
    {
        return;
    }
    //Swap 1st element i,e handle the first case or for n case and write the recurive statement
    //for the next case without worrying it will work or not.
    swap(s[i], s[n - i - 1]);
    reverseString(s, i + 1);
}

int main()
{
    string s = "How old is Santa ?";
    reverseString(s);
    cout << s;
    return 0;
}