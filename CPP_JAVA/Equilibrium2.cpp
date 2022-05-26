#include <iostream>
using namespace std;

int equi(int a[], int n, int sum)
{
    int sum_left = 0;
    for (int i = 0; i < n; i++)
    {

        sum = sum - a[i];
        if (sum == sum_left)
        {
            return (i + 1);
        }
        sum_left = sum_left + a[i];
    }
    return (-1);
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {

        int i, n, sum = 0;
        cin >> n;
        int a[n];
        for (i = 0; i < n; i++)
        {
            cin >> a[i];
            sum = sum + a[i];
        }
        cout << equi(a, n, sum) << endl;
    } //code
    return 0;
}