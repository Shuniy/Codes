#include <iostream>
#include <algorithm>
#include <string>
#include <set>

using namespace std;

int main()
{
    string s = "abcdab";
    int count = 0;
    int k = 0;
    int n = s.size();
    int freq[max];
    memset(freq,0,max);
    for (int i = 0; i < n; i++)
    {
        freq[s[i] - "a"]++;
    }
    int cut = 0;
    if (k = 0)
    {
        for (int i = 0; i < max; i++)
        {
            if (freq[i] > 1)
            {
                cut += freq[i] * (freq[i] - 1)/2;
            }
            else
            {
                for (int i = 0; i < max; i++)
                {
                    if (freq[i] > 0 && i + k < max && freq[i + k] > 0)
                    {
                        cut += freq[i] * freq[i + k];
                    }
                }
            }
        }
    }
}