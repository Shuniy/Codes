package Reboot.SlidingWindow;

import java.util.HashMap;

public class MaximumWindowSubstring {
    public static void main(String[] args) {
        String s = "ADOBECODEBANC";
        String t = "ABC";
        System.out.println(minimumWindowSubstring(s, t));

        s = "a";
        t = "a";
        System.out.println(minimumWindowSubstring(s, t));

        s = "a";
        t = "aa";
        System.out.println(minimumWindowSubstring(s, t));
    }

    public static String minimumWindowSubstring(String s, String t) {
        String string = new String();
        int i = 0;
        HashMap<Character, Integer> hashMap = new HashMap<>();
        int minLen = Integer.MAX_VALUE;
        
        for (Character c : t.toCharArray()) {
            if (hashMap.containsKey(c)) {
                hashMap.put(c, hashMap.get(c) + 1);
            } else {
                hashMap.put(c, 1);
            }
        }
        int count = hashMap.size();
        for (int j = 0; j < s.length(); j++) {
            if (hashMap.containsKey(s.charAt(j))) {
                hashMap.put(s.charAt(j), hashMap.get(s.charAt(j)) - 1);
                if (hashMap.get(s.charAt(j)) == 0) {
                    count -= 1;
                }
            }
            if (count == 0) {
                while (count == 0) {
                    if (minLen > j - i + 1) {
                        minLen = Math.min(minLen, j - i + 1);
                        string = s.substring(i, j + 1);
                    }
                    if (hashMap.containsKey(s.charAt(i))) {
                        hashMap.put(s.charAt(i), hashMap.get(s.charAt(i)) + 1);
                        if (hashMap.get(s.charAt(i)) == 1) {
                            count += 1;
                        }
                    }
                    i += 1;
                }
            }
        }
        return string;
    }
}
