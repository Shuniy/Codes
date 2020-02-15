#include <iostream>

using namespace std;

int ex1 (int n, int m)
{
    if (m == 0)
    {
        return 1;
    }
    else
    {
        return ex1(n, m - 1) * n;
    }
}

int ex2(int n, int m)
{
    if (m == 0)
    {
        return 1;
    }
    else if (m % 2 == 0)
    {
        return ex2(n * n, m / 2);
    }
    else
    {
        return n * ex2(n * n, (m - 1) / 2);
    }
}

int main ()
{
    cout << "Enter the number : ";
    int n;
    cin >> n;
    cout << endl;
    cout << "Enter the power of that number : ";
    int m;
    cin >> m;
    cout << endl;
    cout << "Value of " << n << " to the power " << n << " is : "<< ex2(n, m);
    return 0;
}