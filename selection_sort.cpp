#include <iostream>
#include <algorithm>
#include <random>
#include <cstdlib>
#include <vector>

using namespace std;

void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

vector<int> selection_sort(vector<int> a)
{
    int i, j, min, pos;
    for (i = 0; i < a.size(); i++)
    {
        min = i;
        for (j = i + 1; j < a.size(); j++)
        {
            if (a[j] < a[min])
            {
                min = j;
            }
        }
        swap(&a[min], &a[i]);
    }
    return a;
}

int main()
{
    cout << "How many random numbers to generate : ";
    int n;
    cin >> n;

    vector<int> a;
    for (int i = 0; i < n; i++)
    {
        a.push_back(rand());
    }
    cout << "Generated numbers are : " << endl;
    for (auto i = a.begin(); i != a.end(); i++)
        cout << *i << " ";

    a = selection_sort(a);

    cout << endl
         << "Sorted numbers are : " << endl;
    for (auto i = a.begin(); i != a.end(); i++)
        cout << *i << " ";

    return 0;
}