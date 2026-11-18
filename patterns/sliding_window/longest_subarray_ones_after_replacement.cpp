#include <iostream>
#include <vector>

using namespace std;

class ReplacingOnes
{
public:
    static int findLength(const vector<int> &arr, int k)
    {
        int maxLength = 0, windowStart = 0, maxOnesCount = 0;
        for (int windowEnd = 0; windowEnd < arr.size(); windowEnd++)
        {
            if (arr[windowEnd] == 1)
            {
                maxOnesCount++;
            }
            if (windowEnd - windowStart + 1 - maxOnesCount > k)
            {
                if (arr[windowStart] == 1)
                {
                    maxOnesCount--;
                }
                windowStart++;
            }
            maxLength = max(maxLength, windowEnd - windowStart + 1);
        }
        return maxLength;
    }
};

int main()
{
    cout << "Length after replacing 0s: " << ReplacingOnes::findLength(vector<int>{0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1}, 2) << endl;
    cout << "Length after replacing 0s: " << ReplacingOnes::findLength(vector<int>{0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1}, 3) << endl;
}