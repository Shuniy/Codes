#include <iostream>
#include <unordered_map>

using namespace std;

class CharacterReplacement
{
public:
    static int findLength(const string &str, int k)
    {
        int maxLength = 0, windowStart = 0, maxRepeatLetterCount = 0;
        unordered_map<char, int> letterFrequencyMap;
        for (int windowEnd = 0; windowEnd < str.length(); windowEnd++)
        {
            char rightChar = str[windowEnd];
            letterFrequencyMap[rightChar]++;
            maxRepeatLetterCount = max(maxRepeatLetterCount, letterFrequencyMap[rightChar]);
            if (windowEnd - windowStart + 1 - maxRepeatLetterCount > k)
            {
                char leftChar = str[windowStart];
                letterFrequencyMap[leftChar] -= 1;
                windowStart++;
            }
            maxLength = max(maxLength, windowEnd - windowStart + 1);
        }
        return maxLength;
    }
};

int main()
{
    cout << "Length of the largest string after replacement: " << CharacterReplacement::findLength("aabccbb", 2) << endl;
    cout << "Length of the largest string after replacement: " << CharacterReplacement::findLength("abbcb", 1) << endl;
    cout << "Length of the largest string after replacement: " << CharacterReplacement::findLength("abccde", 1) << endl;
}