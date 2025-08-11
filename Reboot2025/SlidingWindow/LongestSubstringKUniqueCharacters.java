package Reboot.SlidingWindow;

import java.util.HashMap;

public class LongestSubstringKUniqueCharacters {
    public static void main(String[] args) {
        String s = "aabacbebebe";
        int k = 3;
        System.out.println(longestSubstringkUniqueCharacters(s, k));
    }
    public static int longestSubstringkUniqueCharacters(String s, int k) {
        int i = 0;
        int maxLen = Integer.MIN_VALUE;
        HashMap<Character, Integer> hashMap = new HashMap<>();
        for (int j = 0; j < s.length(); j++) {
            Character c = s.charAt(j);
            if (hashMap.containsKey(s.charAt(j))) {
                hashMap.put(c, hashMap.get(c) + 1);
            } else {
                hashMap.put(c, 1);
            }
            if (hashMap.size() < k) {
                continue;
            } else if (hashMap.size() == k) {
                maxLen = Math.max(maxLen, j - i + 1);
            } else {
                while (hashMap.size() > k) {
                    if (hashMap.containsKey(s.charAt(i))) {
                        hashMap.put(s.charAt(i), hashMap.get(s.charAt(i)) - 1);
                        if (hashMap.get(s.charAt(i)) == 0) {
                            hashMap.remove(s.charAt(i));
                        }
                    }
                    i += 1;
                }
            }
        }
        return maxLen;
    }
}
