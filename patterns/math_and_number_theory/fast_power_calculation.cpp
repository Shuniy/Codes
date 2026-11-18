#include <iostream>
#include <algorithm>

#define ll long long

using namespace std;

ll fastPower(int a, int b)
{
    ll result = 1;
    while (b > 0)
    {
        if (b & 1)
        {
            result = a * result;
        }
        a = a * a;
        b = b >> 1;
    }
    return result;
}

int main()
{
    ll a, b;
    cin >> a >> b;
    cout <<"Power is : " << fastPower(a, b);
}