#include <iostream>

using namespace std;

void perm(char s[], int k)
{
    static int a[10] = {0};
    static char res[10];
    if (s[k] == "\0")
    {
        res[k] = '\0';
        cout << res;
    }
    else
    {
        for (int i = 0; s[i] != '\0'; i++)
        {
            if (a[i] == 0)
            {
                res[k] = s[i];
                a[i] = 1;
                perm(s, k + 1);
                a[i] = 0;
            }
        }
    }
}

//Algorithm
void perm2(char s[], int l, int h)
{
    if (l == h)
    {
        cout << s;
    }
    else
    {
        for (int i = l; i <= h; i++)
        {
            swap(s[l], s[i]);
            perm2(s, l+1, h);
            swap(s[l], s[i]);
        }
    }
}

int main ()
{
    char s[] = "ABC";
    perm(s, 0);
    return 0;
}