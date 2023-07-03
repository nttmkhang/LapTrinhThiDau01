#include<iostream>
using namespace std;

long long power(long long a, long long b)
{
    long long t = 1LL;
    while (b > 0)
    {
        if (b % 2 != 0)
            t *= a;
        b /= 2;
        a *= a;
    }
    return t;
}