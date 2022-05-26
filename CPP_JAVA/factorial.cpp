#include <iostream>

using namespace std;

double fact(double n)
{
    int fac;
    if (n == 0)
    {
        return 1;
    }
    else
    {
        fac = fact(n - 1) * n;
    }
    return fac;
}

int main ()
{
    cout << "Enter the number for factorial : ";
    double n;
    cin >> n;
    cout << endl;

    cout << "Factorial is : " << fact(n);
    return 0;
}