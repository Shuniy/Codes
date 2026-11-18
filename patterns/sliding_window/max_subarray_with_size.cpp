#include <iostream>
#include <vector>

using namespace std;

class MaxSumSubarrayOfSizeK
{
public:
    static int findMaxSumSubArray(int k, const vector<int> &arr)
    {
        int windowSum = 0, maxSum = 0;
        int windowStart = 0;
        for (int windowEnd = 0; windowEnd < arr.size(); windowEnd++)
        {
            windowSum += arr[windowEnd];
            if (windowEnd - windowStart + 1 >= k)
            {
                maxSum = max(maxSum, windowSum);
                windowSum -= arr[windowStart];
                windowStart++;
            }
        }
        return maxSum;
    }
};

int main()
{
    cout << "Maximum sum of subarray of size k: " << MaxSumSubarrayOfSizeK::findMaxSumSubArray(3, vector<int>{2, 1, 5, 1, 3, 2}) << endl;
    cout << "Maximum sum of subarray of size k: " << MaxSumSubarrayOfSizeK::findMaxSumSubArray(2, vector<int>{2, 3, 4, 1, 5}) << endl;
    return 0;
}