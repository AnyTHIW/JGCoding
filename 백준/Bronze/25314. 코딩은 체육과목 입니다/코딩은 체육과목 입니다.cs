using System;

// 입력 : 첫 번째 줄에는 문제의 정수 N이 주어진다. (4 < N < 1000, N은 4의 배수 )

// 출력 : 혜아가 N바이트 정수까지 저장할 수 있다고 생각하는 정수 자료형의 이름을 출력하여라.

// 출력에서 long과 long, long과 int 사이에는 공백이 하나씩 들어간다.
// 실제로 C++에서 각 정수 자료형이 저장할 수 있는 수의 크기는 환경에 따라 달라질 수 있다. 덧붙여, 실제로 문제 내용과 같이 long long long int와 같은
// 자료형을 사용한 코드를 GCC의 C++ 컴파일러를 사용해 컴파일하려고 할 경우 'long long long' is too long for GCC라는 에러 메시지와 함께 컴파일되지 않는다.

namespace aaa
{
    class Program
    {
        static int nNumber = 0;

        static int result;

        static void Main(string[] args)
        {
            nNumber = int.Parse(Console.ReadLine() ?? "0");

            result = Calculate(nNumber);
            PrintByteNumber(result);

        }

        static int Calculate(int number)
        {
            int nByteNumber = number / 4;
            int residue = number % 4;

            if (residue != 0)
            {
                nByteNumber += 1;
            }

            return nByteNumber;
        }

        static void PrintByteNumber(int number)
        {
            string stringsOutput = "";

            for (int n = 0; n < number; n++)
            {
                stringsOutput += "long ";
            }

            stringsOutput += "int";

            Console.WriteLine(stringsOutput);

        }

    }
}