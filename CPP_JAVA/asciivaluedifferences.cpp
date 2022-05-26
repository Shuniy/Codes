#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    string a, b;
    a = "Shubham";
    b = "Kumar";
    if (strcmp(a, b) == 0)
    {
        cout << "Impossible";
    }
    else
    {
        cout << "possible";
    }
    int z = strcmp(a, b);
    cout << z;
    return 0;
}