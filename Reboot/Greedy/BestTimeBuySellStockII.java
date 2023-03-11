package Reboot.Greedy;

public class BestTimeBuySellStockII {
    public static void main(String[] args) {
        int[] prices1 = { 7, 1, 5, 3, 6, 4 };
        System.out.println(maxProfit(prices1));
        int[] prices2 = { 1, 2, 3, 4, 5 };
        System.out.println(maxProfit(prices2));
    }
    public static int maxProfit(int[] prices) {
        int result = 0;
        for (int i = 0; i < prices.length - 1; i++) {
            if (prices[i + 1] > prices[i]) {
                result += prices[i + 1] - prices[i];
            }
        }
        return result;
    }
}
