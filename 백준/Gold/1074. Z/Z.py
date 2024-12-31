import sys

input = sys.stdin.readline

_N, _r, _c = map(int, input().split())
# _r(row), _c(column)은 0-based idx 이다.

idx = 0

def DandC(indices, row, col):
    global idx

    if indices == 0:
        return 0
    elif indices == 1:
        
        for j in range(0, 2):
            for i in range(0, 2):
                if j == row and i == col:
                    return idx
                idx += 1
        return idx
    else:
        size = (1 << indices)
        half = (size >> 1)
        
        if row >= half:
            if col >= half:
                idx += (half ** 2) * 3
                return DandC(indices-1, row - half, col-half)
            else:
                idx += (half ** 2) * 2
                return DandC(indices-1, row - half, col)
        else:
            if col >= half:
                idx += (half ** 2)
                return DandC(indices-1, row, col-half)
            else:
                return DandC(indices-1, row, col)

print(DandC(_N, _r, _c))