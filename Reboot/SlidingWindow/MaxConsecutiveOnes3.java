package Reboot.SlidingWindow;

public class MaxConsecutiveOnes3 {
    public static void main(String[] args) {
        int[] nums1 = {1,1,1,0,0,0,1,1,1,1,0}; 
        int k = 2;
        System.out.println(longestOnes(nums1, k));
        int[] nums2 = { 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1 };
        k = 3;
        System.out.println(longestOnes(nums2, k));
    }
    
    public static int longestOnes(int[] nums, int k) {
        int i = 0;
        int result = 0;
        int count = 0;
        for (int j = 0; j < nums.length; j++) {
            if (nums[j] == 0) {
                count += 1;
            }
            if (count < k) {
                result = Math.max(result, j - i + 1);
                continue;
            } else if (count == k) {
                result = Math.max(result, j - i + 1);
            } else {
                while (count > k) {
                    if (nums[i] == 0) {
                        count -= 1;
                    }
                    i += 1;
                }
                result = Math.max(result, j - i + 1);
            }
        }
        return result;
    }
}
