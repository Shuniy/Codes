package Reboot.Greedy;

public class LemonadeChange {
    public static void main(String[] args) {
        int[] bills1 = { 5, 5, 5, 10, 20 };
        System.out.println(lemonadeChange(bills1));
        int[] bills2 = { 5, 5, 10, 10, 20 };
        System.out.println(lemonadeChange(bills2));
        int[] bills3 = { 5, 5, 5, 20 };
        System.out.println(lemonadeChange(bills3));
    }
    public static boolean lemonadeChange(int[] bills) {
        int five = 0;
        int ten = 0;
        for (int item : bills) {
            if (item == 5) {
                five += 1;
            }
            else if (item == 10) {
                if (five <= 0) {
                    return false;
                } else {
                    five -= 1;
                    ten += 1;
                }
            }
            else if (item == 20) {
                if (five <= 0 && ten <= 0) {
                    return false;
                } else if (ten > 0) {
                    ten -= 1;
                    if (five <= 0) {
                        return false;
                    } else {
                        five -= 1;
                    }
                } else {
                    if (five >= 3) {
                        five -= 3;
                    } else {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}
