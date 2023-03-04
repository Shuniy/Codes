package Reboot.SlidingWindow;

import java.util.HashMap;

public class SubarraysKDifferentIntegers {
    public static void main(String[] args) {
        int[] nums1 = {1,2,1,2,3}; 
        int k = 2;
        System.out.println(subarraysWithKDistinct(nums1, k));
        int[] nums2 = { 1, 2, 1, 3, 4 };
        k = 3;
        System.out.println(subarraysWithKDistinct(nums2, k));
    }
    
    public static int subarraysWithKDistinct(int[] nums, int k) {
        int result = 0;
        int i = 0;
        HashMap<Integer, Integer> hashMap = new HashMap<>();

        for (int j = 0; j < nums.length; j++) {
            hashMap.put(nums[j], hashMap.getOrDefault(nums[j], 0) + 1);
            if (hashMap.size() < k) {
                continue;
            } else if (hashMap.size() == k) {
                result += 1;
            } else {
                while (hashMap.size() > k) {
                    if (hashMap.containsKey(nums[i])) {
                        hashMap.put(nums[i], hashMap.get(nums[i]) - 1);
                        result += 1;
                    }
                    if (hashMap.get(nums[i]) == 0) {
                        hashMap.remove(nums[i]);
                    }
                    i += 1;
                }
            }
        }
        return result;
    }
}
