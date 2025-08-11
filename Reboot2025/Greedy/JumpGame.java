package Reboot.Greedy;

public class JumpGame {
    public static void main(String[] args) {
        int[] nums1 = { 2, 3, 1, 1, 4};
        System.out.println(canJump(nums1));
        System.out.println(canJumpHelper(nums1, 0));
        int[] nums2 = { 3, 2, 1, 0, 4 };
        System.out.println(canJump(nums2));
        System.out.println(canJumpHelper(nums2, 0));
        int[] nums3 = { 1, 0, 1, 0 };
        System.out.println(canJump(nums3));
        System.out.println(canJumpHelper(nums3, 0));
    }
    public static boolean canJumpHelper(int[] nums, int index) {
        if (index == nums.length - 1) {
            return true;
        }
        boolean result = false;
        for (int i = 1; i <= nums[index]; i++) {
            if ((index + i) < nums.length) {
                result = result || canJumpHelper(nums, index + i);
            }
        }
        return result;
    }

    public static boolean canJump(int[] nums) {
        int reachable = 0;
        int current = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            if (reachable < i) {
                return false;
            }
            current = i + nums[i];
            reachable = Math.max(reachable, current);
        }
        return reachable >= nums.length - 1;
    }
}
