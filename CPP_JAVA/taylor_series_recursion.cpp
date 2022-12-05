#include <iostream>

using namespace std;

// O(n^2)
float taylor1 (int m, int n)
{
    float p = 1, f = 1;
    float r;
    if (n == 0)
    {
        return 1;
    }
    else
    {
        r = taylor1(m, n - 1);
        p = p * m;
        f = f * n;
        return r + p/f;
    }
}

// O(n)
float taylor2(int m, int n)
{
    static float s;
    if (n == 0)
    {
        return s;
    }
    else
    {
        s = 1 + m * s/n;
        return taylor2(m, n - 1);
    }
}

int main ()
{
    cout << "Enter the number of terms in the series : ";
    int n, m;
    cin >> n;
    cout << endl;
    cout << "Enter the value of x in the series : ";
    cin >> m;
    cout << endl;
    cout << "Value of taylor series upto " << n << " terms is : " << taylor2(m, n);
    return 0;
}