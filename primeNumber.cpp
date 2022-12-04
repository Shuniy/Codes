#include <iostream>
#include <algorithm>

using namespace std;

//Prime Number less than equal to n using seive of eratosthenes
void sieveoferathohenes(int n)
{
    bool prime[n + 1];
    for (int p = 2; p * p <= n; i++)
    {
        if (prime[p] == true)
        {
            for (int i = p * p; i <= n; i += p)
            {
                prime[i] = false;
            }
        }
    }
    for (int p = 2; p <= n; p++)
    {
        if (prime[p])
        {
            cout << p << " ";
        }
    }
}

int main()
{
    int n;
    cout << "Enter a number : ";
    cin >> n;
    if (n <= 1)
    {
        return false;
    }
    if (n <= 3)
    {
        return true;
    }
    if (n % 2 == 0 || n % 3 == 0)
    {
        return false;
    }
    for (int i = 5; i * i <= n; i += 6)
    {
        if (n % i == 0 || n % (i + 2) == 0)
        {
            return false;
        }
    }
    return 0;
}