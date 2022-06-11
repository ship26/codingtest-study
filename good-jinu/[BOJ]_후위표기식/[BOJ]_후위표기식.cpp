#include <stdio.h>
#include <stack>
#include <cstring>
using namespace std;

typedef struct oplvl
{
    char ope;
    int lvl;
}oplvl;

void f(char* str, int len)
{
    stack<oplvl> st;
    oplvl citem, nitem;
    int bracketlvl = 0;
    for (int i = 0; i < len; i++)
    {
        if (str[i] >= 'A' && str[i] <= 'Z')
        {
            putchar(str[i]);
            continue;
        }
        if (str[i] == '(')
        {
            bracketlvl++;
            continue;
        }
        if (str[i] == ')')
        {
            bracketlvl--;
            continue;
        }
        nitem.ope = str[i];
        nitem.lvl = bracketlvl;
        while (!st.empty())
        {
            citem = st.top();
            if (citem.lvl < nitem.lvl)
                break;
            if ((citem.ope == '+' || citem.ope == '-') && (nitem.ope == '/' || nitem.ope == '*') && (citem.lvl == nitem.lvl))
                break;
            putchar(citem.ope);
            st.pop();
        }
        st.push(nitem);
    }
    while (!st.empty())
    {
        putchar(st.top().ope);
        st.pop();
    }
}

int main()
{
    char str[101];
    fgets(str, sizeof(str), stdin);
    f(str, strlen(str) - 1);
    return 0;
}