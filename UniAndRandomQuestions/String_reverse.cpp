#include <iostream>
#include <bits/stdc++.h>
#include <string>
using namespace std;

void reverse(char *s)
{
    if (*s)
    {
        reverse(s + 1);
        cout << *s;
    }
}

void reverseStr(string &str)
{
    int n = str.length();
    for (int i = 0; i < n / 2; i++)
    {
        swap(str[i], str[n - i - 1]);
    }
}

int main()
{
    char s[50];
    cout << "Enter string : ";
    gets(s);
    cout << s;
    cout << endl;
    cout << "Reversed string is : ";
    reverse(s);
    cout << endl;
    string s1;
    cout << "Enter string : ";
    getline(cin, s1);
    cout << "Reversed string is : ";
    reverseStr(s1);
    cout << s1;
    return 0;
}