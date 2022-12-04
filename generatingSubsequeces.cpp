#include <iostream>
#include <string>
#include <set>

using namespace std;

//Easy One using recursion See Ninjas video
void subsequence(string input, string output)
{
    if (input.length() == 0)
    {
        cout << output << endl;
        return;
    }
    subsequence(input.substr(1), output);
    subsequence(input.substr(1), output + input[0]);
}

int main()
{
    string s = "aabc";
    string o = "";
    subsequence2(s, o);
    return 0;
}