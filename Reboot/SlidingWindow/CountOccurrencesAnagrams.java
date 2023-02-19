package Reboot.SlidingWindow;

import java.util.HashMap;

public class CountOccurrencesAnagrams {
    public static void main(String[] args) {
        String text = "forxxorfxdofr";
        String word = "for";
        System.out.println(countOccurrencesAnagrams(text, word));
    }
    public static int countOccurrencesAnagrams(String text, String word) {
        int i = 0;
        int k = word.length();
        int result = 0;
        HashMap<Character, Integer> hashmap = new HashMap<>();
        for (char item: word.toCharArray()) {
            if (hashmap.containsKey(item)) {
                hashmap.put(item, hashmap.get(item) + 1);
            } else {
                hashmap.put(item, 1);
            }
        }
        int hashmapCount = hashmap.size();
        for (int j = 0; j < text.length(); j++) {
            if (hashmap.containsKey(text.charAt(j))) {
                hashmap.put(text.charAt(j), hashmap.get(text.charAt(j)) - 1);
                if (hashmap.get(text.charAt(j)) == 0) {
                    hashmapCount -= 1;
                }
            }
            if ((j - i + 1) < k) {
                continue;
            } else {
                if (hashmapCount == 0) {
                    result += 1;
                }
                if (hashmap.containsKey(text.charAt(i))) {
                    hashmap.put(text.charAt(i), hashmap.get(text.charAt(i)) + 1);
                    if (hashmap.get(text.charAt(i)) == 0) {
                        hashmapCount += 1;
                    }
                }
                i += 1;
            }
        }
        return result;
    }
}
