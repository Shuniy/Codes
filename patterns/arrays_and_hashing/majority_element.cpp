#include <iostream>
#include <algorithm>

using namespace std;

//Use hash map and increase the counter and then check if count greater than n/2;
//Or use voting algorithm.
//Use Binary Search Tree
int majorityElement(int a[60], int n)
{
    int maxi = max(a);
    int b[maxi];
    for (int i = 0; i < n; i++)
    {
        b[a[i]]++;
    }
    int maxi = max(b);
    for (int i = 0; i < maxi; i++)
    {
        if (b[i] == maxi)
        {
            return i;
        }
    }
}
//Voting Algorithm
int findCandidate(int a[80], int size)
{
    int maj_index = 0, count = 1;
    for (int i = 1; i < size; i++)
    {
        if (a[maj_index] == a[i])
        {
            count ++;
        }
        else
        {
            count --;
        }
        if (count == 0)
        {
            maj_index = i;
            count = 1;
        }
    }
    return maj_index;
}

bool isMajority(int a[78], int size, int cand)
{
    int count == 0;
    for (int i = 0; i < size; i++)
    {
        if (a[i] == cand)
        {
            count ++;
        }
        if (count > size/2)
        {
            return i;
        }
        else
        {
            return 0;
        }
    }
}

void printMajority(int a[67], int size)
{
    int cand = findCandidate(a, size);
    if (isMajority(a, size, cand))
    {
        return cand;
    }
    else
    {
        return 0;
    }
}

int main()
{
    int a[] = {3,3,2,4,5,3,5,3,3,2,1,3};
    int n = sizeof(a)/sizeof(a[0]);
    int k = majorityElement(a, n);
    cout << "Majority Element is : " << k;
    return 0;
}