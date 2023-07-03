#include<iostream>
using namespace std;

long long Catalan(long long n)
{
    if (n <= 1)
        return 1;
    long long temp = 0;
    for (long long i = 0; i < n; i++)
        temp += Catalan(i) * Catalan(n - i - 1);
    return temp;
}
