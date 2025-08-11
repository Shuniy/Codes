package Reboot.SlidingWindow;

import java.util.HashMap;

public class LongestSubstringWithoutRepeatingCharacters {
    public static void main(String[] args) {
        String string = "abcabcbb";
        System.out.println(longestSubstringWithoutReapeatingCharacters(string));

        string =  "bbbbbbbbb";
        System.out.println(longestSubstringWithoutReapeatingCharacters(string));

        string = "pwwkew";
        System.out.println(longestSubstringWithoutReapeatingCharacters(string));
    }
    public static int longestSubstringWithoutReapeatingCharacters(String string) {
        int i = 0;
        HashMap<Character, Integer> hashMap = new HashMap<>();
        int maxLen = Integer.MIN_VALUE;
        for (int j = 0; j < string.length(); j++) {
            Character c = string.charAt(j);
            if (hashMap.containsKey(c)) {
                hashMap.put(c, hashMap.get(c) + 1);
            } else {
                hashMap.put(c, 1);
            }
            if (hashMap.size() == j - i + 1) {
                maxLen = Math.max(maxLen, j - i + 1);
            } else if (hashMap.size() < j - i + 1) {
                while (hashMap.size() < j - i + 1) {
                    if (hashMap.containsKey(string.charAt(i))) {
                        hashMap.put(string.charAt(i), hashMap.get(string.charAt(i)) - 1);
                        if (hashMap.get(string.charAt(i)) == 0) {
                            hashMap.remove(string.charAt(i));
                        }
                    }
                    i += 1;
                }
            }
        }
        if (maxLen < 0) {
            return 0;
        } else {
            return maxLen;
        }
    }
}
