package Reboot.Greedy;

import java.util.HashMap;
import java.util.PriorityQueue;

public class HandOfStraights {
    public static void main(String[] args) {
        int[] hand1 = { 1, 2, 3, 6, 2, 3, 4, 7, 8 }; 
        int groupSize = 3;
        System.out.println(isNStraightHand(hand1, groupSize));
        int[] hand2 = { 1, 2, 3, 4, 5 }; 
        groupSize = 3;
        System.out.println(isNStraightHand(hand2, groupSize));
    }
    public static boolean isNStraightHand(int[] hand, int groupSize) {
        if (hand.length % groupSize > 0) {
            return false;
        }
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        for (Integer integer : hand) {
            hashMap.put(integer, hashMap.getOrDefault(integer, 0) + 1);
        }
        for (Integer integer : hashMap.keySet()) {
            minHeap.add(integer);
        }
        while (minHeap.size() > 0) {
            int first = minHeap.peek();
            for (int i = first; i < first + groupSize; i++) {
                if (!hashMap.containsKey(i)) {
                    return false;
                }
                hashMap.put(i, hashMap.get(i) - 1);
                if (hashMap.get(i) == 0) {
                    if (i != minHeap.peek()) {
                        return false;
                    }
                    minHeap.remove();
                }
            }
        }
        return true;
    }
}
