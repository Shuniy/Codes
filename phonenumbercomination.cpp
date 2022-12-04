#include <iostream>
#include <vector>
#include <bits/stdc++.h>
#include <string>
using namespace std;

void findCombinations(auto const &keypad, auto const &input, string res, int index)
{
    if (index == -1)
    {
        cout << res << " ";
        return;
    }
    int digit = input[index];
    int len = keypad[digit].size();
    for (int  i = 0; i < len; i++)
    {
        findCombinations(keypad, input, keypad[digit][i] + res, index - 1);
    }
}

int main()
{
    vector<char> keypad[] =
        {
            {}, {}, {'A', 'B', 'C'}, {'D', 'E', 'F'}, {'G', 'H', 'I'}, {'J', 'K', 'L'}, {'M', 'N', 'O'}, {'P', 'Q', 'R', 'S'}, {'T', 'U', 'V'}, {'W', 'X', 'Y', 'Z'}};

    int input[] = {2, 3, 4};
    int n = sizeof(input) / sizeof(input[0]);

    findCombinations(keypad, input, string(""), n - 1);

    return 0;
}