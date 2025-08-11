package Reboot.SlidingWindow;

import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class FirstNegativeNumberWindowSizeK {
    public static void main(String[] args) {
        int arr[] = {12, -1, -7, 8, -15, 30, 16, 28};
        int n = arr.length;
        int k = 3;
        System.out.println(firstNegativeNumberWindowSizeK(arr, k, n));
    }
    public static List<Integer> firstNegativeNumberWindowSizeK(int[] arr, int k, int n) {
        int i = 0;
        List<Integer> result = new LinkedList<Integer>();
        Queue<Integer> queue = new LinkedList<Integer>();
        for (int item: arr) {
            if (item < 0) {
                queue.add(item);
            }
        }
        for (int j = 0; j < n; j++) {
            if (queue.size() == 0) {
                result.add(0);
            } else {
                result.add(queue.peek());
                if (queue.peek() == arr[i]) {
                    queue.remove();
                }
                i += 1;
            }
        }
        return result;
    }
}