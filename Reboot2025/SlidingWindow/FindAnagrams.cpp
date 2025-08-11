#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class StringAnagrams
{
public:
    static vector<int> findStringAnagrams(const string &str, const string &pattern)
    {
        int windowStart = 0, matched = 0;
        vector<int> resultIndices{};
        unordered_map<char, int> charFrequencyMap;
        for (auto chr : pattern)
        {
            charFrequencyMap[chr]++;
        }
        for (int windowEnd = 0; windowEnd < str.length(); windowEnd++)
        {
            char rightChar = str[windowStart];
            if (charFrequencyMap.find(rightChar) != charFrequencyMap.end())
            {
                charFrequencyMap[rightChar]--;
                if (charFrequencyMap[rightChar] == 0)
                {
                    matched++;
                }
            }

            if (matched == (int)charFrequencyMap.size())
            {
                resultIndices.push_back(windowStart);
            }
            if (windowEnd >= pattern.length() - 1)
            {
                char leftChar = str[windowStart];
                windowStart++;
                if (charFrequencyMap.find(leftChar) != charFrequencyMap.end())
                {
                    if (charFrequencyMap[leftChar] == 0)
                    {
                        matched--;
                    }
                }
                charFrequencyMap[leftChar]++;
            }
        }
        return resultIndices;
    }
};

int main()
{
    auto result = StringAnagrams::findStringAnagrams("pqqp", "pq");
    for (auto num : result)
    {
        cout << num << " ";
    }
    cout << endl;
    result = StringAnagrams::findStringAnagrams("abbcabc", "abc");
    for (auto num : result)
    {
        cout << num << " ";
    }
    cout << endl;
}