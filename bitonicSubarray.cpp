#include <iostream>
#include <algorithm>

using namespace std;

//O(n) Space 
void bitonicSubarray(int a[90], int n)
{
    int I[n + 1], D[n + 1];
    I[0] = 1;
    for (int i = 1; i <= n; i++)
    {
        I[i] = 1;
        if (a[i - 1] < a[i])
        {
            I[i] = I[i - 1] + 1;
        }
    }
    D[n] = 1;
    for (int j = n; j >= 0; j--)
    {
        D[j] = 1;
        if (a[j + 1] < a[j])
        {
            D[j] = D[j + 1] + 1;
        }
    }
    int len = 1;
    int beg = 0;
    int end = 0;
    for (int i = 0; i <= n; i++)
    {
        len = I[i] + D[i] -1;
        beg = i - I[i] + 1;
        end = i + D[i] -1;
    }
    cout <<"Start : " << a[beg] << " end" << a[end] << "lenght : " << len;
}

//without O(n) Space
voidbitonicSubarray(int a[90], int n)
{
    int end = 0;
    int maxLen = 0;
    int i = 0;
    while (i + 1 < n)
    {
        int len = 1;
        while (i + 1 < n && a[i] < a[i + 1])
        {
            len ++;
            i ++;
        }
        while (i + 1 < n && a[i] > a[i + 1])
        {
            len++;
            i++;
        }
        if (len > maxLen)
        {
            maxLen = len;
            end = i;
        }
    }
    cout << "find between : " << end - maxLen + 1 << " and " << end;
}

int main()
{
    int a[] = {12,4,78,90,45,23};
    int n = sizeof(a)/sizeof(a[0]);
    bitonicSubarray(a, n);
    return 0;
}