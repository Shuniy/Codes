#include <iostream>

using namespace std;

int Sum (int n)
{
    int nextNumber;
    if (n == 0 || n == 1)
    {
        return n;
    }
    else
    {
        return Sum(n - 1) + n;
    }
}

int main ()
{
    cout << "Enter the number of terms : ";
    int n;
    cin >> n;
    cout << endl;
    cout << "Sum of " << n << "natural numbers is : "<< Sum(n);
    return 0;
}