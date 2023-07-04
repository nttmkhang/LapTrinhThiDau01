#include<iostream>
using namespace std;

float LuyThua(float x, long n)
{
    float t = 1;
    while (n > 0)
    {
        if (n % 2 != 0)
            t *= x;
        x *= x;
        n /= 2;
    }
    return t;
}