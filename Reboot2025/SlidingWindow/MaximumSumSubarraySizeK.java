package Reboot.SlidingWindow;

class Solution {
    public static void main(String[] args) {
        int[] arr = {1, 4, 2, 10, 2, 3, 1, 0, 20};
        int k = 3;
        int n = arr.length;
        System.out.println(maximumSubSubarraySizeK(arr, n, k));
    }
    public static int maximumSubSubarraySizeK(int[] arr, int n, int k) {
        int i = 0;
        int currentSum = 0;
        int maxSum = 0;
        for (int j = 0; j < n; j++) {
            currentSum += arr[j];
            if ((j - i + 1) < k) {
                continue;
            } else {
                maxSum = Math.max(currentSum, maxSum);
                currentSum -= arr[i];
                i += 1;
            }
        }
        return maxSum;
    }
}