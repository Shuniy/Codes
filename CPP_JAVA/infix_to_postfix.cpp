#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <cstring>

const int size = 50;

using namespace std;

char infix[size], postfix[size], stack[size];
int top = -1;

int precedence(char ch);
char pop();
char top_element();
void push(char ch);
int braces(char *);

int main()
{
    char ele, elem, st[2];
    int prep, pre, popped, j = 0, chk = 0;
    strcpy(postfix, " ");
    cout << "ASSUMPTION : Infix expression contains single letter variables and single digit constants only " << endl;
    cout << "Enter infix expression....." << endl;
    gets(infix);
    chk = braces(infix);
    if (chk != 0)
    {
        cout << "Unbalanced no. of braces.....";
        cout << (chk == 1 ? "right braces" : "left braces") << endl;
        exit(1);
    }
    for (int i = 0; infix[i] != '\0'; i++)
    {
        if (infix[i] != '(' && infix[i] != '^' && infix[i] != '*' && infix[i] != '/' && infix[i] != '+' && infix[i] != '-')
        {
            postfix[j++] = infix[i];
        }
        else if (infix[i] == '(')
        {
            elem = infix[i];
            push(elem);
        }
        else if (infix[i] == ')')
        {
            while ((popped = pop()) != '(')
            {
                postfix[j++] = popped;
            }
        }
        else
        {
            elem = infix[i];
            pre = precedence(elem);
            ele = top_element();
            prep = precedence(ele);
            if (pre > prep)
            {
                push(elem);
            }
            else
            {
                while (prep >= pre)
                {
                    if (ele == '#')
                    {
                        break;
                    }
                    popped = pop();
                    ele = top_element();
                    postfix[j++] = popped;
                    prep = precedence(ele);
                }
                push(elem);
            }
        }
    }
    while ((popped = pop()) != '#')
    {
        postfix[j++] = popped;
    }
    postfix[j] = '\0';
    cout << endl
         << "postfix : " << postfix << endl;
    return 0;
}

int precedence(char ch)
{
    switch (ch)
    {
    case '^':
        return 5;
    case '/':
        return 4;
    case '*':
        return 3;
    case '+' :
        return 3;
    case '-' :
        return 3;
    default:
        return 0;
    }
}

char pop()
{
    char ret;
    if (top != -1)
    {
        ret = stack[top];
        top--;
        return ret;
    }
    else
    {
        return '#';
    }
}

char top_element()
{
    char ch;
    if (top != -1)
    {
        ch = stack[top];
    }
    else
    {
        ch = '#';
    }
    return ch;
}

void push(char ch)
{
    if (top != size - 1)
    {
        top++;
        stack[top] = ch;
    }
}

int braces(char *s)
{
    int leftbr, rightbr;
    leftbr = rightbr = 0;
    for (int i = 0; s[i]; i++)
    {
        if (s[i] == '(')
        {
            leftbr++;
        }
        else if (s[i] == ')')
        {
            rightbr++;
        }
    }
    if (leftbr == rightbr)
    {
        return 0;
    }
    else if (leftbr < rightbr)
    {
        return 1;
    }
    else
    {
        return -1;
    }
}
