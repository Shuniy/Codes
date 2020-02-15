#include <iostream>
#include <algorithm>
#include <bits/stdc++.h>

using namespace std;

/*
I have a nested list, and I need to reverse every element in the list. But I dont
know whether the list is a list of list of list or not. So example is:
p = [1, [2, 3, [4, [5, 6]]]]
print deep_reverse(p)
#>>> [[[[6, 5], 4], 3, 2], 1]

q =  [1, [2,3], 4, [5,6]]
print deep_reverse(q)
#>>> [ [6,5], 4, [3, 2], 1]
*/

//Just a logic code doesn't work.......
int * deepReverse(int &a)
{
    if(a.length() == 0)
    {
        return a;
    }
    else if(type(a) == int)
    {
            return a;
    }
    else
    {
        return deepReverse(a[1:]) + [deepReverse(a[0])];
    }
}

int main()
{
    int a= [[ [ [ 6, 5 ], 4 ], 3, 2 ], 1];
    int b = [ [ 6, 5 ], 4, [ 3, 2 ], 1 ];
    cout << deepReverse(a);
    cout << deepReverse(b);
    return 0;
}