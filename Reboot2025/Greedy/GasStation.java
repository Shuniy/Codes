package Reboot.Greedy;
import java.util.Arrays;

public class GasStation {
    public static void main(String[] args) {
        int[] gas1 = { 1, 2, 3, 4, 5 }; 
        int[] cost1 = { 3, 4, 5, 1, 2 };
        System.out.println(canCompleteCircuit(gas1, cost1));
        int[] gas2 = { 2, 3, 4 }; 
        int[] cost2 = { 3, 4, 3 };
        System.out.println(canCompleteCircuit(gas2, cost2));
    }
    public static int canCompleteCircuit(int[] gas, int[] cost) {
        if (Arrays.stream(gas).sum() < Arrays.stream(cost).sum()) {
            return -1;
        }
        int tank = 0;
        int resultIndex = 0;
        for (int i = 0; i < cost.length; i++) {
            tank += gas[i] - cost[i];
            if (tank < 0) {
                tank = 0;
                resultIndex = i + 1;
            }
        }
        return resultIndex;
    }
}
