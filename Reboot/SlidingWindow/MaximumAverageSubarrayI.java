package Reboot.SlidingWindow;

public class MaximumAverageSubarrayI {
    public static void main(String[] args) {
        int[] nums1 = {1,12,-5,-6,50,3}; 
        int k = 4;
        System.out.println(findMaxAverage(nums1, k));
        int[] nums2 = {5};
        k = 1;
        System.out.println(findMaxAverage(nums2, k));
        int[] nums3 = { -1 };
        k = 1;
        System.out.println(findMaxAverage(nums3, k));
    }
    public static double findMaxAverage(int[] nums, int k) {
        int i = 0;
        double result = Double.NEGATIVE_INFINITY;
        double sum = 0.0;

        for (int j = 0; j < nums.length; j++) {
            sum += nums[j];
            if ((j - i + 1) < k) {
                continue;
            } else if ((j - i + 1) == k) {
                result = Math.max(result, sum / k);
            } else {
                sum -= nums[i];
                result = Math.max(result, sum / k);
                i += 1;
            }
        }
        return result;
    }
}