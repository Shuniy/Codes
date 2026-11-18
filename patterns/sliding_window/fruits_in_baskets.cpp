#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class MaxFruitCountOf2Types
{
public:
    static int findLength(const vector<char> &arr)
    {
        int maxLength = 0, wordStart = 0;
        unordered_map<char, int> fruitFrequencyMap;

        for (int wordEnd = 0; wordEnd < arr.size(); wordEnd++)
        {
            fruitFrequencyMap[arr[wordEnd]]++;
            while ((int)fruitFrequencyMap.size() > 2)
            {
                char leftChar = arr[wordStart];
                fruitFrequencyMap[leftChar]--;
                if (fruitFrequencyMap[leftChar] == 0)
                {
                    fruitFrequencyMap.erase(leftChar);
                }
                wordStart++;
            }
            maxLength = max(maxLength, wordEnd - wordStart + 1);
        }
        return maxLength;
    }
};

int main()
{
    cout << "Maximum number of fruits: " << MaxFruitCountOf2Types::findLength(vector<char>{'A', 'B', 'C', 'A', 'C'}) << endl;
    cout << "Maximum number of fruits: " << MaxFruitCountOf2Types::findLength(vector<char>{'A', 'B', 'C', 'B', 'B', 'C'}) << endl;
}