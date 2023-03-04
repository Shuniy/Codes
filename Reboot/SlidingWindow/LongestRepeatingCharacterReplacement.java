package Reboot.SlidingWindow;

import java.util.HashMap;

public class LongestRepeatingCharacterReplacement {
    public static void main(String[] args) {
        String s = "ABAB"; 
        int k = 2;
        System.out.println(characterReplacement(s, k));
        s = "AABABBA";
        k = 1;
        System.out.println(characterReplacement(s, k));
        s = "AAAA";
        k = 2;
        System.out.println(characterReplacement(s, k));
    }

    public static int characterReplacement(String s, int k) {
        int i = 0;
        HashMap<Character, Integer> hashMap = new HashMap<>();
        int maxCount = 0;
        int result = 0;
        for (int j = 0; j < s.length(); j++) {
            hashMap.put(s.charAt(j), hashMap.getOrDefault(s.charAt(j), 0) + 1);
            maxCount = Math.max(maxCount, hashMap.get(s.charAt(j)));
            if ((j - i + 1 - maxCount) < k) {
                result = Math.max(result, j - i + 1);
                continue;
            } else if ((j - i + 1 - maxCount) == k) {
                result = Math.max(result, j - i + 1);
            } else {
                if (hashMap.containsKey(s.charAt(i))) {
                    hashMap.put(s.charAt(i), hashMap.get(s.charAt(i)) - 1);
                }
                if (hashMap.get(s.charAt(i)) == 0) {
                    hashMap.remove(s.charAt(i));
                }
                if ((j - i + 1 - maxCount) == k) {
                    result = Math.max(result, j - i + 1);
                }
                i += 1;
            }
        }
        return result;
    }
}
