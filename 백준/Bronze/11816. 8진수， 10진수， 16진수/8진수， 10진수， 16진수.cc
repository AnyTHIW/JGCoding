#include <iostream>
#include <string>
using namespace std;
string _N;

char check_radix(string str);
void change_deci_into_radix(string number, char radix);

main()
{
    cin >> _N;
    char radix = check_radix(_N);
    change_deci_into_radix(_N, radix);
}

char
check_radix(string str)
{
    if (str[0] == '0' && str[1] == 'x')
        return 'x';
    else if (str[0] == '0')
        return '8';
    else
        return '1';
}

void
change_deci_into_radix(string str, char radix)
{
    if (radix == 'x')
    {
        cout << stoi(str.substr(2), NULL, 16);
    }
    else if (radix == '8')
    {
        cout << stoi(str.substr(1), NULL, 8);
    }
    else
    {
        cout << stoi(str, NULL, 10);
    }

    return;
}