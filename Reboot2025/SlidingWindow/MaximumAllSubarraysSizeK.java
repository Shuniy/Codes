package Reboot.SlidingWindow;

import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class MaximumAllSubarraysSizeK {
    public static void main(String[] args) {
        int[] nums = {1, 3, -1, -3, 5, 3, 6, 7};
        int k = 3;
        System.out.println(maximumAllSubarraysSizeK(nums, k));
    }

    public static List<Integer> maximumAllSubarraysSizeK(int[] nums, int k) {
        int i = 0;
        List<Integer> result = new LinkedList<>();
        Queue<Integer> queue = new LinkedList<Integer>();
        for (int item : nums) {
            queue.add(item);
        }
        for (int j = 0; j < nums.length; j += 1) {
            if (queue.size() > 0) {
                while ((queue.size() > 0) && queue.peek() < nums[j]) {
                    queue.remove();
                }
            }
            if ((j - i + 1) < k) {
                continue;
            } else {
                result.add(queue.peek());
                if (queue.peek() == nums[i]) {
                    queue.remove();
                }
                i += 1;
            }
        }
        return result;
    }
}
