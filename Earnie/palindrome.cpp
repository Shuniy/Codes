#include <iostream>

using namespace std;

boolean palindrome(int n)
{
    int r, n, remainder;
    while (n != 0)
    {
        r = n % 10;
        reverse = reverse * 10 + r;
        n = n / 10;
    }
    if (reverse == n)
    {
        return true;
    }
    else
    {
        return false;
    }
}

int main ()
{
    cout << "Enter a number : ";
    int n;
    cin >>  n;
    bool k = palindrome(n);
    if (k == true)
    {
        cout << "Number is palindrome ";
    }
    else
    {
        cout << "Not palindrome ";
    }
    return 0;
}