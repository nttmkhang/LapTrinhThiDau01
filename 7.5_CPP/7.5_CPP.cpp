#include<iostream>
using namespace std;

typedef string BigNum;

int toNumber(char c)
{
    if (c == '0')
        return 0;
    if (c == '1')
        return 1;
    if (c == '2')
        return 2;
    if (c == '3')
        return 3;
    if (c == '4')
        return 4;
    if (c == '5')
        return 5;
    if (c == '6')
        return 6;
    if (c == '7')
        return 7;
    if (c == '8')
        return 8;
    if (c == '9')
        return 9;
    if (c == 'A' || c == 'a')
        return 10;
    if (c == 'B' || c == 'b')
        return 11;
    if (c == 'C' || c == 'c')
        return 12;
    if (c == 'D' || c == 'd')
        return 13;
    if (c == 'E' || c == 'e')
        return 14;
    return 15;
}

char toChar(int n)
{
    char Letter[] = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F' };
    return Letter[n];
}


BigNum subBigNum(BigNum x, BigNum y)
{
    while (x.size() < y.size())
        x = '0' + x;
    while (x.size() > y.size())
        y = '0' + y;

    int borrow = 0;
    BigNum temp = "";
    for (int i = x.size() - 1; i >= 0; i--)
    {
        int xx = toNumber(x[i]);
        int yy = toNumber(y[i]);
        int ss = xx - yy - borrow;
        if (ss < 0)
        {
            ss += 10;
            borrow = 1;
        }
        else
            borrow = 0;
        temp = toChar(ss) + temp;
    }
    while (temp.size() > 1 && temp[0] == '0')
        temp.erase(0, 1);
    return temp;
}
