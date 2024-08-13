import sys

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_Three_Strings = [ _.rstrip() for _ in IFSs() ]

lastNumber = 0
for i in range(3):
    if _Three_Strings[i] not in ["Fizz", "Buzz", "FizzBuzz"]:
        lastNumber = int(_Three_Strings[i]) + 3 - i

if lastNumber %5 == 0 and lastNumber % 3 == 0:
    print("FizzBuzz")
elif lastNumber%3==0:
    print("Fizz")
elif lastNumber%5==0:
    print("Buzz")
else:
    print(lastNumber)