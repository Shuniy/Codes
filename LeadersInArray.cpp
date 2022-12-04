#include <iostream>
#include <algorithm>

using namespace std;
//Use Two loops
//Or start from right and first print the last element
void leaderArray(int a[60], int n)
{
    int maxRight = a[n-1];
    cout << maxRight;
    for (int i = n - 2; i >= 0; i--)
    {
        if (maxRight < a[i])
        {
            maxRight = a[i];
            cout << maxRight << " ";
        }
    }
}

int main()
{
    int a[] = {9, 4,5,3,2,1};
    int n = sizeof(a)/ sizeof(a[0]);
    leaderArray(a, n);
    return 0;
}