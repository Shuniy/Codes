#include <iostream>
#include <algorithm>
#include <bits/stdc++.h>

using namespace std;

/*
A Simple Solution is to consider every pair and keep track maximum product.

A Better Solution is to use sorting. Below are detailed steps.
1) Sort input array in increasing order.
2) If all elements are positive, then return product of last two numbers.
3) Else return maximum of products of first two and last two numbers.

An Efficient Solution can solve the above problem in single traversal of input array. The idea is to traverse the input array and keep track of following four values.
a) Maximum positive value
b) Second maximum positive value
c) Maximum negative value i.e., a negative value with maximum absolute value
d) Second maximum negative value.
At the end of the loop, compare the products of first two and last two and print the maximum of two products. 
*/
void findMaxProduct(int a[80], int n)
{
    int max1 = a[0];
    int max2 = INT_MIN;
    int min1 = a[0];
    int min2 = INT_MAX;
    for (int i = 1; i < n; i++)
    {
        if(max1 < a[i])
        {
            max2 = max1;
            max1 = a[i];
        }
        else if(max2 < a[i])
        {
            max2 = a[i];
        }
        if (a[i] < min1)
        {
            min2 = min1;
            min1 = a[i];
        }
        else if (a[i] < min2)
        {
            min2 = a[i];
        }
    }
    if (max1 * max2 > min1 * min2)
    {
        cout << "Pair is : "<<max1 << " ," << max2 << endl;
    }
    else
    {
        cout << "Pair is : " << min1 << " ," << min2 << endl;
    }
}

int main()
{
    int a[] = {-10, -3, 5, 6, -2, 2};
    int n = sizeof(a)/sizeof(a[0]);
    findMaxProduct(a, n);
    return 0;
}