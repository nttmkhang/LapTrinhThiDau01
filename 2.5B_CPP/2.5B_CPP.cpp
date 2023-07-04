#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool isPrime(long long);
string outVector(vector<long long>);
vector<long long> findPrime(long long);

int main()
{
    long long n;
    cout << "Nhap n (n <= 10^9): ";
    cin >> n;
    cout << "\nCac so nguyen to nho hon bang ";
    cout << n << " la: ";
    cout << outVector(findPrime(n));

    cout << "\n\n\nKet thuc!!!!";
    return 1;
}

bool isPrime(long long n)
{
    int dem = 0;
    for (long long i = 1; i <= n; i++)
        if (n % i == 0)
            dem++;
    return (dem == 2);
}

string outVector(vector<long long> a)
{
    string temp;
    long long i = 0;
    while (i < a.size())
    {
        temp = temp + " " + to_string(a[i]);
        i++;
    }
    return temp;
}

vector<long long> findPrime(long long n)
{
    vector<long long> prime;
    for (long long p = 2; p <= n; p++)
        if (isPrime(p))
            prime.push_back(p);
    return prime;
}