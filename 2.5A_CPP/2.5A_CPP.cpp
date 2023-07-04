#include <iostream>
#include <vector>
using namespace std;

bool isPrime(long long n)
{
    int dem = 0;
    for (long long i = 1; i <= n; i++)
        if (n % i == 0)
            dem++;
    return (dem == 2);
}

vector<long long> findPrime(long long n)
{
    vector<long long> prime;
    for (long long p = 2; p <= n; p++)
        if (isPrime(p))
            prime.push_back(p);
    return prime;
}