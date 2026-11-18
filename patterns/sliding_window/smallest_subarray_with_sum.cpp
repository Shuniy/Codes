#include <iostream>
#include <vector>
#include <limits>

using namespace std;

class MinSizeSubarraySum {
public:
    static int findMinSubArray(int S, const vector<int> &arr)
    {
        int windowSum = 0, minLength = numeric_limits<int>::max();
        int windowStart = 0;
        for (int windowEnd = 0; windowEnd < arr.size(); windowEnd++)
        {
            windowSum += arr[windowEnd];
            while (windowSum >= S)
            {
                minLength = min(minLength, windowEnd - windowStart + 1);
                windowSum -= arr[windowStart];
                windowStart++;
            }
        }
        return minLength == numeric_limits<int>::max() ? 0 : minLength;
    }
};

int main(int argc, char *argv[])
{
    int result = MinSizeSubarraySum::findMinSubArray(7, vector<int>{2, 1, 5, 2, 3, 2});
    cout << "Smallest subarray length: " << result << endl;
    result = MinSizeSubarraySum::findMinSubArray(7, vector<int>{2, 1, 5, 2, 8});
    cout << "Smallest subarray length: " << result << endl;
    result = MinSizeSubarraySum::findMinSubArray(8, vector<int>{3, 4, 1, 1, 6});
    cout << "Smallest subarray length: " << result << endl;
    return 0;
}