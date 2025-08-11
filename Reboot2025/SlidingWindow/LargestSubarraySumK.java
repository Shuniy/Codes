package Reboot.SlidingWindow;

import java.util.HashMap;

public class LargestSubarraySumK {
    public static void main(String[] args) {
        int[] arr = {10, 5, 2, 7, 1, 9};
        int k = 15;
        System.out.println(largestSubarraySumK(arr, k));
        System.out.println(largestSubarraySumKHashmap(arr, k));
    }
    public static int largestSubarraySumK(int[] arr, int k) {
        int i = 0;
        int currentSum = 0;
        int maxLen = 0;
        for (int j = 0; j < arr.length; j++) {
            currentSum += arr[j];
            if (currentSum < k) {
                continue;
            } else if (currentSum == k) {
                maxLen = Math.max(maxLen, j - i + 1);
            } else {
                while (currentSum > k) {
                    currentSum -= arr[i];
                    i += 1;
                }
                if (currentSum == k) {
                    maxLen = Math.max(maxLen, j - i + 1);
                }
            }
        }
        return maxLen;
    }
    public static int largestSubarraySumKHashmap(int[] arr, int k) {
        HashMap<Integer, Integer> hashmap = new HashMap<>();
        int currentSum = 0;
        int maxLen = 0;
        for (int i = 0; i < arr.length; i++) {
            currentSum += arr[i];
            if (currentSum == k) {
                maxLen = Math.max(maxLen, i + 1);
            } else if (hashmap.containsKey(currentSum - k)) {
                maxLen = Math.max(maxLen, i - hashmap.get(currentSum - k));
            }
            if (hashmap.containsKey(currentSum) == false) {
                hashmap.put(currentSum, i);
            }
        }
        return maxLen;
    }
}
