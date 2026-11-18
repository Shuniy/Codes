#include <iostream>
#include <algorithm>

using namespace std;

//Find last indeces of an element
int lastIndex(int a[90], int n, int x, int currIndex)
{
    if (currIndex == n)
    {
        return -1;
    }
    int index = lastIndex(a, n, x, currIndex + 1);
    if (index == -1 && a[currIndex] == x)
    {
        return currIndex;
    }
    else
    {
        return index;
    }
}

int main()
{
    int a[] = {1,2,3,2,2,5};
    int x = 2;
    int n = sizeof(a)/sizeof(a[0]);
    cout << lastIndex(a, n, x, 0);
    return 0;
}