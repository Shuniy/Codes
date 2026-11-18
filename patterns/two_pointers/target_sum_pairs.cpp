#include <iostream>
#include <algorithm>

using namespace std;

//Use two loops or use this one
void pairedElements(int a[90], int targetSum)
{
    int low = 0;
    int hight = n -1;
    sort(a, a+n);
    while (low < high)
    {
        if (arr[low] + arr[high] == sum)
        {
            cout << "pair at : " << a[low] <<" , " << a[high];
        }
        if (arr[low] + arr[high] > sum)
        {
            high --;
        }
        else
        {
            low ++;
        }
    }
}

//Use hashing
void pairedElements()

int main()
{
    int arr[] = {2, 3, 4, -2, 6, 8, 9, 11};
    pairedElements(arr, 6);
    return 0;
}