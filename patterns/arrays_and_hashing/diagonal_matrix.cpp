#include <iostream>
using namespace std;

struct matrix
{
    int a[10];
    int n;
};

void set(struct matrix * m, int i, int j, int x)
{
    if (i == j)
    {
        m -> a[i] = x;
    }
    m -> a[i] = x;
}

int get(struct matrix m, int i, int j)
{
    if (i == j)
    {
        return m.a[i];
    }
    else
    {
        return 0;
    }
}

void display(struct matrix m)
{
    int i, j;
    for (i = 0; i < m.n; i++)
    {
        for (j = 0; j < m.n; j++)
        {
            if (i == j)
            {
                cout << m.a[i] << " ";
            }
            else
            {
                cout << "0 ";
            }
        }
        cout << endl;
    }
}

int main()
{
    struct matrix m;
    m.n = 4;
    set(&m, 0, 0, 5);
    set(&m, 1, 1, 8);
    set(&m, 2, 2, 9);
    set(&m, 3, 3, 12);
    get(m, 1, 1);
    display(m);
}