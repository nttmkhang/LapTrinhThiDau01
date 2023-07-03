#include<iostream>
using namespace std;

long long countDivisors_3(long long);

int main()
{
	return 0;
}

long long countDivisors_3(long long n)
{
    long long T = 1;
    long long p = 2;
    while (n > 1 && p * p <= n)
    {
        long long count = 0;
        while (n % p == 0)
        {
            count++;
            n /= p;
        }
        T = T * (count + 1);
        p++;
    }
    if (n > 1)
        T = T * 2;
    return T;
}
