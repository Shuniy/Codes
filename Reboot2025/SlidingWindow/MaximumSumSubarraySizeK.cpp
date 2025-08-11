#include<stdio.h>
#include<iostream>
using namespace std;

int maximumSubSubarraySizeK(int arr[], int k, int n) {
    int i = 0;
    int currentSum = 0;
    int maxSum = 0;
    for (int j = 0; j < n; j++) {
        currentSum += arr[j];
        if ((j - i + 1) < k) {
            continue;
        } else {
            maxSum = max(currentSum, maxSum);
            currentSum -= arr[i];
            i += 1;
        }
    }
    return maxSum;
}

int main() {
    int arr[] = {1, 4, 2, 10, 2, 3, 1, 0, 20};
    int k = 3;
    int n = sizeof(arr)/sizeof(arr[0]);
    cout << "Maximum Subarray sum of size k: " << maximumSubSubarraySizeK(arr, k, n) << endl;    
    return 0;
}