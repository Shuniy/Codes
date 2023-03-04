package Reboot.SlidingWindow;

import java.util.HashMap;

public class SubstringsSize3DistinctCharacters {
    public static void main(String[] args) {
        String s = "aababcabc";
        System.out.println(countGoodSubstrings(s));
    }
    public static int countGoodSubstrings(String s) {
        int i = 0;
        int count = 0;
        HashMap<Character, Integer> hashMap = new HashMap<>();
        for (int j = 0; j < s.length(); j++) {
            if (hashMap.containsKey(s.charAt(j))) {
                hashMap.put(s.charAt(j), hashMap.get(s.charAt(j)) + 1);
            } else {
                hashMap.put(s.charAt(j), 1);
            }

            if ((j - i + 1) < 3) {
                continue;
            } else if ((j - i + 1) == 3) {
                if (hashMap.size() == 3) {
                    count += 1;
                }
            } else {
                if (hashMap.containsKey(s.charAt(i))) {
                    hashMap.put(s.charAt(i), hashMap.get(s.charAt(i)) - 1);
                }
                if (hashMap.get(s.charAt(i)) == 0) {
                    hashMap.remove(s.charAt(i));
                }
                if (hashMap.size() == 3) {
                    count += 1;
                }
                i += 1;
            }
        }
        return count;
    }
}
