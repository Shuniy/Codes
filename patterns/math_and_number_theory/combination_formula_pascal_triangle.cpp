#include <iostream>

using namespace std;

float nCr(int n, int r)
{
    if (r == 0 || r == n)
    {
        return 1;
    }
    else
    {
        return nCr(n - 1, r - 1) + nCr(n - 1, r);
    }
}

int main ()
{
    cout << "Enter n : ";
    int r, n;
    cin >> n;
    cout << endl << "Enter r with r <= n :";
    cin >> r;
    cout << endl << "nCr for values provided is : " << nCr(n, r);
    return 0;
}