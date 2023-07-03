#include<iostream>
using namespace std;

long long Fibonacci(long long n)
{
    if (n == 0)
        return 0;
    if (n == 1)
        return 1;
    long long Ftt = 0;
    long long Ft = 1;
    long long i = 2;
    long long Fhh = 0;
    while (i <= n)
    {
        Fhh = Ft + Ftt;
        i++;
        Ftt = Ft;
        Ft = Fhh;
    }
    return Fhh;
}
