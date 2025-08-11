package Reboot.Greedy;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Stack;

public class RemoveDuplicateLetters {
    public static void main(String[] args) {
        String s = "bcabc";
        System.out.println(removeDuplicateLettersMonotonicStack(s));
        System.out.println(removeDuplicateLettersGreedy(s));
        s = "cbacdcbc";
        System.out.println(removeDuplicateLettersMonotonicStack(s));
        System.out.println(removeDuplicateLettersGreedy(s));
    }
    public static String removeDuplicateLettersGreedy(String s) {
        int[] cnt = new int[26];
        int pos = 0;
        for (int i = 0; i < s.length(); i++) { 
            cnt[s.charAt(i) - 'a'] += 1;
        }
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) < s.charAt(pos)) { 
                pos = i;
            }
            cnt[s.charAt(i) - 'a'] -= 1;
            if (cnt[s.charAt(i) - 'a'] == 0) {
                break;
            }
        }
        return s.length() == 0 ? "" : s.charAt(pos) + removeDuplicateLettersGreedy(s.substring(pos + 1).replaceAll("" + s.charAt(pos), ""));
    }
    public static String removeDuplicateLettersMonotonicStack(String s) {
        HashMap<Character, Integer> frequency = new HashMap<Character, Integer>();
        for (Character itemCharacter : s.toCharArray()) {
            frequency.put(itemCharacter, frequency.getOrDefault(itemCharacter, 0) + 1);
        }
        HashSet<Character> set = new HashSet<>();
        Stack<Character> stack = new Stack<>();
        String result = "";
        for (int i = 0; i < s.length(); i++) {
            if (set.contains(s.charAt(i))) {
                frequency.put(s.charAt(i), frequency.get(s.charAt(i)) - 1);
                continue;
            }
            while (!stack.empty() && s.charAt(i) < stack.peek() && frequency.get(stack.peek()) != 0) {
                set.remove(stack.pop());
            }
            frequency.put(s.charAt(i), frequency.get(s.charAt(i)) - 1);
            set.add(s.charAt(i));
            stack.add(s.charAt(i));
        }
        for (Character character : stack) {
            result = result + character;
        }
        return result;
    }
}