package Reboot.SlidingWindow;

import java.util.HashMap;

public class ContainsDuplicate {
    public static void main(String[] args) {
        int[] nums1 = {1,2,3,1}; 
        int k = 3;
        System.out.println(containsNearbyDuplicate(nums1, k));
        int[] nums2 = {1,0,1,1}; 
        k = 1;
        System.out.println(containsNearbyDuplicate(nums2, k));
        int[] nums3 = {1,2,3,1,2,3}; 
        k = 2;
        System.out.println(containsNearbyDuplicate(nums3, k));
    }
    
    public static boolean containsNearbyDuplicate(int[] nums, int k) {
        int i = 0;
        if (k < nums.length) {
            k = k + 1;
        } else {
            k = nums.length;
        }
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        for (int j = 0; j < nums.length; j++) {
            if (hashMap.containsKey(nums[j])) {
                hashMap.put(nums[j], hashMap.get(nums[j]) + 1);
            } else {
                hashMap.put(nums[j], 1);
            }
            if ((j - i + 1) < k) {
                continue;
            } else if ((j - i + 1) == k) {
                if (hashMap.size() < k) {
                    return true;
                }
            } else {
                if (hashMap.containsKey(nums[i])) {
                    hashMap.put(nums[i], hashMap.get(nums[i]) - 1);
                }
                if (hashMap.get(nums[i]) == 0) {
                    hashMap.remove(nums[i]);
                }
                if (hashMap.size() < k) {
                    return true;
                }
                i += 1;
            }
        }
        return false;
    }
}
