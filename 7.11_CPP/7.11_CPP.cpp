#include<iostream>
using namespace std;

typedef string BigNum;

BigNum modBigNum(BigNum x, BigNum y)
{
    BigNum kY[11];
    kY[0] = "0";
    for (int i = 1; i <= 10; i++)
        kY[i] = addBigNum(kY[i - 1], y);

    BigNum hold = "";
    for (int i = 0; i < x.size(); i++)
    {
        hold = hold + x[i];
        int k = 0;
        while (compareBigNum(hold, kY[k + 1]) >= 0)
            k++;
        hold = subBigNum(hold, kY[k]);
    }
    return hold;
}
