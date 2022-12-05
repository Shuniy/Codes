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

vector <int> bubble_sort(vector <int> a)
{
    int i, j;
    for (i = 0; i < a.size() - 1; i++)
        for (j = 0; j < a.size() - i - 1; j++)
            if (a[j] > a[j + 1])
                swap(&a[j], &a[j + 1]);
    return a;
}

int main ()
{
    cout << "How many random numbers to generate : ";
    int n;
    cin >> n;

    vector <int> a;
    for (int i = 0; i < n; i++)
    {
        a.push_back(rand());
    }
    cout << "Generated numbers are : " << endl;
    for (auto i = a.begin(); i != a.end(); i++)
        cout << *i << " ";
        
    a = bubble_sort(a);

    cout << endl << "Sorted numbers are : " << endl;
    for (auto i = a.begin(); i != a.end(); i++)
        cout << *i << " ";
    
    return 0;
}