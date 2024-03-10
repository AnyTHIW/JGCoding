import sys
IFS = sys.stdin.readline

_N, _K = map(int, IFS().split())

# 이항계수 공식  = !N / !(N-K) * !K

exclamationMul = 1

for i in range(1, _N+1):
    exclamationMul *= i
                                                                                                                                                                                                                                                                                                                                                                                                      
for i in range(1, _N-_K+1):
    exclamationMul //= i
    
for i in range(1, _K+1):
    exclamationMul //= i
    
print(exclamationMul)