#include <iostream>
#include <algorithm>

using namespace std;

//Make 0 as -1 and 1 as 1 and when sum == 0 then index will be i and end on j - i + 1

int subArray(int a[90], int n)
{
    int sum = 0;
    int maxSize = -1;
    int startindex;
    for (int i = 0; i < n - 1; i++)
    {
        sum = (a[i] == 0) ? -1 : 1;
        for (int j = i + 1; j < n; j++)
        {
            (a[i] == 0) ? sum+=-1 : sum += 1;
            if (sum == 0 && maxSize < j - i + 1)
            {
                maxSize = j - i + 1;
                startindex = i;
            }
        }
    }
    if (maxSize == -1)
    {
        return 0;
    }
    
}

int main()
{
    int arr[] = {0,1,0,0,1,1,0,0,1,1,1};
    int n = sizeof(a)/sizeof(a[0]);
    subArray(a, n);
    return 0;
}