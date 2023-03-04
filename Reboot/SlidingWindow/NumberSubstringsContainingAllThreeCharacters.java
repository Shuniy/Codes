package Reboot.SlidingWindow;

import java.util.HashMap;

public class NumberSubstringsContainingAllThreeCharacters {
    public static void main(String[] args) {
        String s = "abcabc";
        System.out.println(numberOfSubstrings(s));
        s = "aaacb";
        System.out.println(numberOfSubstrings(s));
        s = "abc";
        System.out.println(numberOfSubstrings(s));
    }

    public static int numberOfSubstrings(String s) {
        int result = 0;
        int i = 0;
        int k = 3;
        HashMap<Character, Integer> hashMap = new HashMap<>();

        for (int j = 0; j < s.length(); j++) {
            hashMap.put(s.charAt(j), hashMap.getOrDefault(s.charAt(j), 0) + 1);
            while (hashMap.size() >= k) {
                if (hashMap.containsKey(s.charAt(i))) {
                    hashMap.put(s.charAt(i), hashMap.get(s.charAt(i)) - 1);
                }
                if (hashMap.get(s.charAt(i)) == 0) {
                    hashMap.remove(s.charAt(i));
                }
                i += 1;
            }
            result += i;
        }

        return result;
    }
}
