package Reboot.Greedy;

public class WiggleSubsequence {
    public static void main(String[] args) {
        int[] nums1 = {1,7,4,9,2,5};
        System.out.println(wiggleMaxLength(nums1));
        int[] nums2 = {1,17,5,10,13,15,10,5,16,8};
        System.out.println(wiggleMaxLength(nums2));
    }
    public static int wiggleMaxLength(int[] nums) {
        int up = 1;
        int down = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i - 1]) {
                up = down + 1;
            } else if (nums[i] < nums[i - 1]) {
                down = up + 1;
            }
        }
        return Math.max(up, down);
    }
}
