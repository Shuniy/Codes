#include <iostream>
#include <algorithm>

using namespace std;

void subArraySum(int a[1005], int n, int targetSum)
{
    int start = 0;
    int end = 0;
    for(int i = 0; i < n; i++)
    {
        int currSum = 0;
        if (currSum < targetSum)
        {
            currSum += a[i];
        }
        else if (currSum > targetSum)
        {
            currSum -= a[start];
            start ++;
        }
        else
        {
            end = i;
        }
    }
    cout << "start index is : " << start << " end index is : " << end << endl;
}

int main()
{
    int arr[] = {17, 5, 2, 7, 1, 9};
    int n = sizeof(a)/sizeof(a[0]);
    int targetSum;
    cin >> targetSum;
    subArraySum(a, n, targetSum);
    return 0;
}