#include <iostream>
#include <vector>

using namespace std;

int fib (int n)
{
    if (n == 0 || n == 1)
    {
        return n;
    }
    else
    {
        return fib(n - 1) + fib (n - 2);
    }
}

void display (int n)
{
    for (int i = 0; i < n; i ++)
    {
        cout << fib(i) << " ";
    }
}

int main ()
{
    cout << "Enter the position you want from fibonacci : ";
    int n;
    cin >> n;

    cout << "Number at position " << n << " in Fibonacci series  : ";
    cout << fib(n - 1);
    cout << endl;

    cout << "Enter the limit of the series : ";
    cin >> n;
    cout << endl;
    cout << "Fibonacci series upto position " << n << " is : ";
    display(n);

    return 0;
}