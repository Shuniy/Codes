#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class WordConcatenation
{
public:
    static vector<int> findWordConcatenation(const string &str, const vector<string> words)
    {
        unordered_map<string, int> wordFrequencyMap;
        for (auto word : words)
        {
            wordFrequencyMap[word]++;
        }

        vector<int> resultIndices{};
        int wordsCount = words.size(), wordLength = words[0].length();

        for (int i = 0; i <= str.length() - wordsCount * wordLength; i++)
        {
            unordered_map<string, int> wordSeen;
            for (int j = 0; j < wordsCount; j++)
            {
                int nextWordIndex = i + j * wordLength;
                string word = str.substr(nextWordIndex, wordLength);
                if (wordFrequencyMap.find(word) == wordFrequencyMap.end())
                {
                    break;
                }
                wordSeen[word]++;
                if (wordSeen[word] > wordFrequencyMap[word])
                {
                    break;
                }
                if (j + 1 == wordsCount)
                {
                    resultIndices.push_back(i);
                }
            }
        }
        return resultIndices;
    }
};

int main()
{
    vector<int> result = WordConcatenation::findWordConcatenation("catfoxcat", vector<string>{"cat", "fox"});
    for (auto num : result)
    {
        cout << num << " ";
    }
    cout << endl;
    result = WordConcatenation::findWordConcatenation("catcatfoxfox", vector<string>{"cat", "fox"});
    for (auto num : result)
    {
        cout << num << " ";
    }
    cout << endl;
}