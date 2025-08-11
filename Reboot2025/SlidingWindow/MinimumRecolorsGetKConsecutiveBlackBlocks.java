package Reboot.SlidingWindow;

public class MinimumRecolorsGetKConsecutiveBlackBlocks {
    public static void main(String[] args) {
        String blocks = "WBBWWBBWBW"; 
        int k = 7;
        System.out.println(minimumRecolors(blocks, k));
        blocks = "WBWBBBW"; 
        k = 2;
        System.out.println(minimumRecolors(blocks, k));
    }
    
    public static int minimumRecolors(String blocks, int k) {
        int i = 0;
        int minWhiteCount = Integer.MAX_VALUE;
        int currentCount = 0;
        for (int j = 0; j < blocks.length(); j++) {
            if (blocks.charAt(j) == 'W') {
                currentCount += 1;
            }
            if ((j - i + 1) < k) {
                continue;
            } else if ((j - i + 1) == k) {
                minWhiteCount = Math.min(minWhiteCount, currentCount);
            } else {
                if (blocks.charAt(i) == 'W') {
                    currentCount -= 1;
                }
                minWhiteCount = Math.min(minWhiteCount, currentCount);
                i += 1;
            }
        }
        if (minWhiteCount == Integer.MAX_VALUE) {
            return 0;
        } else {
            return minWhiteCount;
        }
    }
}
