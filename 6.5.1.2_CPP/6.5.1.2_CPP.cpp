#include<iostream>
using namespace std;

long long Tong(long long n)
{
    if (n % 2 == 0)
        return n / 2 * (n + 1);
    return (n + 1) / 2 * n;
}