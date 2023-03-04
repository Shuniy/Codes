package Reboot.SlidingWindow;

public class LongestSubstringOfAllVowelsOrder {
    public static void main(String[] args) {
        String word = "aeiaaioaaaaeiiiiouuuooaauuaeiu";
        System.out.println(longestBeautifulSubstring(word));
        word = "aeeeiiiioooauuuaeiou";
        System.out.println(longestBeautifulSubstring(word));
        word = "a";
        System.out.println(longestBeautifulSubstring(word));
        word = "aeiou";
        System.out.println(longestBeautifulSubstring(word));
    }
    public static int longestBeautifulSubstring(String word) {
        int i = 0;
        int count = 1;
        int result = 0;
        for (int j = 1; j < word.length(); j++) {
            if (word.charAt(j) < word.charAt(j - 1)) {
                i = j;
                count = 1;
            } else if (word.charAt(j) != word.charAt(j - 1)) {
                count += 1;
            }
            if (count == 5) {
                result = Math.max(result, j - i + 1);
            }
        }
        return result;
    }
}
