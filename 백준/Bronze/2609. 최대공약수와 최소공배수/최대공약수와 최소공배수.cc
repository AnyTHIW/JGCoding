#include <iostream>
#include <string.h>
using namespace std;

int get_GCD(int a, int b);
int get_LCM(int a, int b);

main()
{
    int natural_a, natural_b;

    cin >> natural_a >> natural_b;

    cout << get_GCD(natural_a, natural_b) << "\n"
         << get_LCM(natural_a, natural_b);
}

int get_GCD(int a, int b)
{
    int c = a % b;
    while (c != 0)
    {
        a = b;
        b = c;
        c = a % b;
    }
    return b;
}

int get_LCM(int a, int b)
{
    return (a * b) / get_GCD(a, b);
}