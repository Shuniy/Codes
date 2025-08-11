package Reboot.Greedy;

public class JumpGameII {
    public static void main(String[] args) {
        int[] nums1 = { 2, 3, 1, 1, 4 };
        System.out.println(jump(nums1));
        int[] nums2 = { 3, 2, 1, 0, 4 };
        System.out.println(jump(nums2));
        int[] nums3 = { 2, 3, 0, 1, 4 };
        System.out.println(jump(nums3));
        int[] nums4 = { 1, 2, 1, 1, 1 };
        System.out.println(jump(nums4));
    }
    
    public static int jump(int[] nums) {
        int current = 0;
        int reachable = 0;
        int timesChanged = 0;
        int prevReachableIndex = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > reachable) {
                return -1;
            }
            current = i + nums[i];
            reachable = Math.max(current, reachable);
            if (prevReachableIndex == i) {
                timesChanged += 1;
                prevReachableIndex = reachable;
                if (reachable >= nums.length - 1) {
                    return timesChanged;
                }
            }
        }
        return timesChanged;
    }
}
