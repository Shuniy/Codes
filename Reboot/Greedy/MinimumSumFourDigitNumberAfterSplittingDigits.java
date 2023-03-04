package Reboot.Greedy;

import java.util.Arrays;

public class MinimumSumFourDigitNumberAfterSplittingDigits {
    public static void main(String[] args) {
        int num = 2932;
        System.out.println(minimumSum(num));
        num = 4009;
        System.out.println(minimumSum(num));
    }
    public static int minimumSum(int num) {
        String s = String.valueOf(num);
        char[] arr = s.toCharArray();
        Arrays.sort(arr);
        s = String.valueOf(arr);
        String num1 = "";
        String num2 = "";
        for (int i = 0; i < s.length(); i++) {
            if (i % 2 == 0) {
                num1 += s.charAt(i);
            } else {
                num2 += s.charAt(i);
            }
        }
        int numi1 = Integer.parseInt(num1);
        int numi2 = Integer.parseInt(num2);
        return numi1 + numi2;
    }
}
