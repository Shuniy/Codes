#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int Case, n, index = 0;
    vector<int> c;
    cin >> Case;
    while (Case > 0)
    {
        cin >> n;
        int a[n];
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
        }
        int maxCount = 0;
        for (int i = 0; i < n; i++)
        {
            int count = 0;
            for (int j = 0; j < n; j++)
            {
                if (a[i] == a[j])
                {
                    count++;
                }
            }
            if (count > maxCount)
            {
                maxCount = count;
                index = i;
            }
        }
        if (maxCount > n / 2)
        {
            c.push_back(a[index]);
        }
        else
        {
            c.push_back(-1);
        }
        Case--;
    }
    for (auto i = c.begin(); i != c.end(); i++)
    {
        cout << *i << endl;
    }
    return 0;
}