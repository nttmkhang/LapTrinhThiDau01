#include <vector>
#include <string>
using namespace std;

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
