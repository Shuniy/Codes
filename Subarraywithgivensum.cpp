#include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int c = 0; c < t; c++)
    {
        int n, s;
        cin >> n >> s;
        int sum = 0, left = 0, right = -1;
        int *arr = new int[n];
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
            if (right > 0)
                continue;
            sum += arr[i];
            while (sum > s)
            {
                sum -= arr[left];
                left++;
            }
            if (sum == s)
                right = i;
        }
        if (right > 0)
            cout << left + 1 << " " << right + 1 << endl;
        else
            cout << "-1" << endl;
        delete[] arr;
    }

    return 0;
}