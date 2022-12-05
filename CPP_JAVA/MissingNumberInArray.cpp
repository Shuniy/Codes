#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int total, Case, n;
    vector<int> c;
    cin >> Case;
    while (Case > 0)
    {
        cin >> n;
        int a[n];
        total = (n) * (n + 1) / 2;
        for (int i = 0; i < n - 1; i++)
        {
            cin >> a[i];
            total = total - a[i];
        }
        c.push_back(total);
        Case--;
    }
    for (auto i = c.begin(); i != c.end(); i++)
    {
        cout << *i << endl;
    }
    return 0;
}