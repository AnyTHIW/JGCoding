import sys
IFS = sys.stdin.readline

_N = int(IFS().rstrip())

def countSugarBag(kilo):
    dp_BagNum = [-1]*5001 # 0kilo일때 가방갯수 0
#       1kilo일때 가방갯수 0, 2kilo일때 가방갯수 0, 3kilo일때 가방갯수 1
    dp_BagNum[3] = dp_BagNum[5] = 1
    
    for i in range(6, kilo+1 ):
        if i % 5 == 0:
            dp_BagNum[i] = dp_BagNum[i -5] + 1
        elif i % 3 == 0:
            dp_BagNum[i] = dp_BagNum[i-3] + 1
        elif dp_BagNum[i-3] > 0 and dp_BagNum[i-5] > 0:
            dp_BagNum[i] = min(dp_BagNum[i-3], dp_BagNum[i-5]) + 1
    print(dp_BagNum[kilo])

countSugarBag(_N)