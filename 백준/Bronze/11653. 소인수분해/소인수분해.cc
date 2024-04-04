#include <iostream>
using namespace std;
int _N;
int result;

void
print_rec(int big);

main()
{
    cin >> _N;

    print_rec(_N);
}

void
print_rec(int big)
{
    int number = 2;
    while (1 != big)
    {
        if (0 == big % number)
        {
            printf("%d\n", number);
            big /= number;
        }
        else
        {
            number++;
        }
    }
}