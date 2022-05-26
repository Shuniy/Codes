#include <iostream>
#include<algorithm>

using namsepace std;
//Either take the sum of element and subtract it from the sum of terms upto n;

//Else do it position wise take anather array and store element at those positions and traverse to find missing element.
//or if there is difference present then a[i] - i = difference. then compare at any point difference dont match  find element there.
//To prevent overflow in sum we can pick one number to known number and subtract one number from missing number.
int missingElement(int arr[50], int n)
{
    int i, total = 1;
    for (i = 2; i <= n+1; i++)
    {
        total += i;
        total -= a[i-2];
    }
    return total;
}

//Use XOR i,e. 
/*
XOR all elements let the result be x1;
XOR of all elements from 1 to n let it be x2;
XOR of x1 and x2 will give missing number.
*/

int main()
{
    int arr[] = {1,2,4,5,6,7,8};
    int n = sizeof(arr)/sizeof(arr[0]);
    int k = missingElement(arr, n);
    cout << "Missing Element is : "<< k ;
    return 0;
}