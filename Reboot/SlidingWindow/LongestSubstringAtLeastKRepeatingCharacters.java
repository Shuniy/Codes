package Reboot.SlidingWindow;

public class LongestSubstringAtLeastKRepeatingCharacters {
    public static void main(String[] args) {
        String s = "aaabb";
        int k = 3;
        System.out.println(longestSubstring(s, k));
        s = "ababbc";
        k = 2;
        System.out.println(longestSubstring(s, k));
        s = "bbaaacbd";
        k = 3;
        System.out.println(longestSubstring(s, k));
    }
    public static int longestSubstring(String s, int k) {
        int result = 0;
        for (int charsAllowed = 1; charsAllowed <= 26; charsAllowed += 1) {
            int i = 0;
            int found = 0;
            int[] freq = new int[26];
            for (int j = 0; j < freq.length; j++) {
                freq[j] = 0;
            }
            int nonZeroFreq = 0;
            for (int j = 0; j < s.length(); ) {
                if (nonZeroFreq <= charsAllowed) {
                    int ascii = (int) s.charAt(j);
                    int asciiIndex = ascii - 97;
                    freq[asciiIndex] += 1;
                    if (freq[asciiIndex] == 1) {
                        nonZeroFreq += 1;
                    }
                    if (freq[asciiIndex] == k) {
                        found += 1;
                    }
                    j += 1;
                } else {
                    int ascii = (int) s.charAt(i);
                    int asciiIndex = ascii - 97;
                    i += 1;
                    if (freq[asciiIndex] == k) {
                        found -= 1;
                    }
                    freq[asciiIndex] -= 1;
                    if (freq[asciiIndex] == 0) {
                        nonZeroFreq -= 1;
                    }
                }
                if (nonZeroFreq == charsAllowed && found == charsAllowed) {
                    result = Math.max(result, j - i);
                }
            }
        }

        return result;
    }
}
