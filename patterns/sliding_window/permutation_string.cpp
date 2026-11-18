#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

class StringPermutation
{
public:
    static bool findPermutation(const string &str, const string &pattern)
    {
        int windowStart = 0, matched = 0;
        unordered_map<char, int> charFrequencyMap;

        for (auto chr : pattern)
        {
            charFrequencyMap[chr]++;
        }

        for (int windowEnd = 0; windowEnd < str.length(); windowEnd++)
        {
            char rightChar = str[windowEnd];
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
                return true;
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
                    charFrequencyMap[leftChar]++;
                }
            }
        }
        return false;
    }
};

int main()
{
    cout << "Permutation exists: " << StringPermutation::findPermutation("oidbcaf", "abc") << endl;
    cout << "Permutation exists: " << StringPermutation::findPermutation("odicf", "dc") << endl;
    cout << "Permutation exists: " << StringPermutation::findPermutation("bcdxabcdy", "bcdyabcdx") << endl;
    cout << "Permutation exists: " << StringPermutation::findPermutation("aaacb", "abc") << endl;
}