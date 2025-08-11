package Reboot.SlidingWindow;

public class BinarySubarraysWithSum {
    public static void main(String[] args) {
        int[] nums1 = { 1, 0, 1, 0, 1 }; 
        int goal = 2;
        System.out.println(numSubarraysWithSum(nums1, goal));
        int[] nums2 = { 0, 0, 0, 0, 0 }; 
        goal = 0;
        System.out.println(numSubarraysWithSum(nums2, goal));
    }
    public static int numSubarraysWithSum(int[] nums, int goal) {
        return atMost(nums, goal) - atMost(nums, goal - 1);
    }
    public static int atMost(int[] nums, int goal) {
        if (goal < 0) {
            return 0;
        }
        int result = 0;
        int i = 0;
        int sum = 0;
        for (int j = 0; j < nums.length; j++) {
            sum += nums[j];
            while (sum > goal) {
                sum -= nums[i];
                i += 1;
            }
            result += j - i + 1;
        }
        return result;
    }
}
