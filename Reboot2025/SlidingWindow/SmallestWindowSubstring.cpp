#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

class MinimumWindowSubstring
{
public:
    static string findSubstring(const string &str, const string &pattern)
    {
        int windowStart = 0, matched = 0, minLenght = str.length() + 1, subStrStart = 0;
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
                if (charFrequencyMap[rightChar] >= 0)
                {
                    matched++;
                }
            }

            while (matched == pattern.length())
            {
                if (minLenght > windowEnd - windowStart + 1)
                {
                    minLenght = windowEnd - windowStart + 1;
                    subStrStart = windowStart;
                }
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
        return minLenght > str.length() ? "" : str.substr(subStrStart, minLenght);
    }
};

int main()
{
    cout << "Minimum Window Substring: " << MinimumWindowSubstring::findSubstring("aabdec", "abc") << endl;
    cout << "Minimum Window Substring: " << MinimumWindowSubstring::findSubstring("abdabca", "abc") << endl;
    cout << "Minimum Window Substring: " << MinimumWindowSubstring::findSubstring("adcad", "abc") << endl;
}