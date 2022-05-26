#include <iostream>
#include <algorithm>

using namespace std;

int multiply(int n, int * res, int top)
{
    int j = 0;
    int current = 0;
    int carry = 0;
    for (j = 0; j <= top; j++)
    {
        current = n * res[j] + carry;
        res[j] = current % 10;
        carry = current / 10;
    }
    while (carry > 0)
    {
        top = top + 1;
        res[top] = carry % 10;
        carry = carry /10;
    }
    return top;
}

void factorialLarge(int n)
{
    int res[1000];
    res[0] = 1;
    int top = 0;
    for (int i = 2; i <= n; i++)
    {
        top = multiply(i, res, top);
    }
    cout << "Factorial is : " << endl;
    for (int i = top; i >= 0 ; i--)
    {
        cout << res[i];
    }
}

int main()
{
    int n;
    cout<< "Enter a number : ";
    cin >> n;
    factorialLarge(n);
    return 0;
}