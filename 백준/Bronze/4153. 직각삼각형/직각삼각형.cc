#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int a, b, c;
    while (true)
    {
        cin >> a >> b >> c;

        if (a == 0 && b == 0 && c == 0)
            break;
        else
        {
            int max_value = max({a, b, c});

            if (a * a + b * b + c * c == 2 * max_value * max_value)
                cout << "right" << endl;
            else
                cout << "wrong" << endl;
        }
    }

    return 0;
}