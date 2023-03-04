package Reboot.SlidingWindow;

import java.util.LinkedList;
import java.util.Queue;

public class MinimumDifferenceBetweenHighestLowestKScores {
    public static void main(String[] args) {
        int[] nums1 = {90}; 
        int k = 1;
        System.out.println(minimumDifference(nums1, k));
        int[] nums2 = {9,4,1,7};
        k = 2;
        System.out.println(minimumDifference(nums2, k));
    }
    public static int minimumDifference(int[] nums, int k) {
        int i = 0;
        Queue<Integer> currentMin = new LinkedList<>();
        Queue<Integer> currentMax = new LinkedList<>();

        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        int result = Integer.MAX_VALUE;

        for (Integer num : nums) {
            currentMin.add(num);
            currentMax.add(num);
        }

        for (int j = 0; j < nums.length; j++) {
            min = Math.min(min, nums[j]);
            max = Math.max(max, nums[j]);
            if (currentMin.size() > 0) {
                while (currentMin.size() > 0 && currentMin.peek() > min) {
                    currentMin.remove();
                }
            }
            if (currentMax.size() > 0) {
                while (currentMax.size() > 0 && currentMax.peek() < max) {
                    currentMax.remove();
                }
            }
            if ((j - i + 1) < k) {
                continue;
            } else if ((j - i + 1) == k) {
                result = Math.min(result, currentMax.peek() - currentMin.peek());
            } else {
                while (nums[i] == currentMin.peek()) {
                    currentMin.remove();
                }
                while (nums[i] == currentMax.peek()) {
                    currentMax.remove();
                }

                max = currentMax.peek();
                min = currentMin.peek();
                result = Math.min(result, max - min);
                i += 1;
            }
        }
        return result;
    }
}
