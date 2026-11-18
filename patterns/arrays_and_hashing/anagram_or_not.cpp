#include <iostream>

using namespace std;

int main ()
{
    char a[] = "decimal";
    char b[] = "medical";
    int h[26] = {0}, i;

    for (int i = 0; a[i] != '\0'; i++)
    {
        h[a[i] - 97] += 1;
    }

    for (int i = 0; b[i] != '\0' ; i++)
    {
        h[a[i] - 97] -= 1;
        if (h[a[i]] - 97 < 0)
        {
            cout << "Not anagram" << endl;
            break;
        }
    }
    if (b[i] == '\0')
    {
        cout << "Its anagram " << endl;
    }
    return 0;
}