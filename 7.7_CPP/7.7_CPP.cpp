#include <string>
#include <iostream>
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


BigNum mulBigNum(BigNum x, BigNum y)
{
    BigNum temp = "";
    BigNum zero = "";
    for (int i = x.size() - 1; i >= 0; i--)
    {
        long xx = toNumber(x[i]);
        BigNum ss = mulBigNum(y, xx);
        ss = ss + zero;
        temp = addBigNum(temp, ss);
        zero = zero + '0';
    }
    return temp;
}