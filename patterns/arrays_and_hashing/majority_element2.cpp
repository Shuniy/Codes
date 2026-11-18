#include <bits/stdc++.h>
using namespace std;
int main()
{

    int t;
    cin >> t;

    while (t)
    {

        int n;
        cin >> n;
        vector<int> v(n);
        for (int i = 0; i < n; i++)
        {
            cin >> v[i];
        }

        int majority_index = 0;
        int count = 1;

        for (int i = 1; i < n; i++)
        {
            if (v[i] == v[majority_index])
            {
                count++;
            }
            else
            {
                count--;
            }

            if (count == 0)
            {
                majority_index = i;
                count = 1;
            }
        }

        count = 0;
        for (int i = 0; i < n; i++)
        {
            if (v[i] == v[majority_index])
            {
                count++;
            }
        }
        if (count > n / 2)
        {
            cout << v[majority_index] << endl;
        }
        else
        {
            cout << -1 << endl;
        }

        t--;
    }
}