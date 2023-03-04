package Reboot.SlidingWindow;

public class KBeautyString {
    public static void main(String[] args) {
        int num = 240, k = 2;
        System.out.println(divisorSubstrings(num, k));
        num = 430043; 
        k = 2;
        System.out.println(divisorSubstrings(num, k));
    }
    public static int divisorSubstrings(int num, int k) {
        int count = 0;
        int i = 0;
        String s = new String();
        s = String.valueOf(num);
        for (int j = 0; j < s.length(); j++) {
            if ((j - i + 1) < k) {
                continue;
            } else if ((j - i + 1) == k) {
                Integer value = Integer.parseInt(s.substring(i, j + 1));
                if (value != 0) {
                    if ((num % value) == 0) {
                        count += 1;
                    }
                }
            } else {
                i += 1;
                Integer value = Integer.parseInt(s.substring(i, j + 1));
                if (value != 0) {
                    if ((num % value) == 0) {
                        count += 1;
                    }
                }
            }
        }
        return count;
    }
}
