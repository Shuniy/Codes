package Reboot.DynamicProgramming;

public class BestTimeBuySellStock {
    public static void main(String[] args) {
        int[] prices = { 7, 1, 5, 3, 6, 4 };
        System.out.println(maxProfit(prices));
    }
    public static int maxProfit(int[] prices) {
        int[] min = prices.clone();
        int[] max = prices.clone();
        int result = 0;
        for (int i = 0; i < min.length; i++) {
            if (i == 0) {
                continue;
            }
            min[i] = Math.min(min[i - 1], prices[i]);
        }
        for (int i = max.length - 1; i >= 0; i--) {
            if (i == max.length - 1) {
                continue;
            }
            max[i] = Math.max(max[i + 1], prices[i]);
        }
        for (int i = 0; i < prices.length; i++) {
            result = Math.max(result, max[i] - min[i]);
        }
        return result;
    }
}
