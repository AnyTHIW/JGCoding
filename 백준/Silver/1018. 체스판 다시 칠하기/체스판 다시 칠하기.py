import sys

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_N_Line, _M_Column = map(int, IFS().split())
_Arr_NLineInfo = [ _.rstrip() for _ in IFSs() ]

pattern1 = ["WBWBWBWB", "BWBWBWBW"] *4
pattern2 = ["BWBWBWBW", "WBWBWBWB"] *4
minChanges = 2500

def getMinChanges(x, y, board, pattern):
    changes = 0
    for i in range(8):
        for j in range(8):
            if board[x + i][y + j] != pattern[i][j]:
                changes += 1
    return changes

for i in range(_N_Line - 7):
    for j in range(_M_Column - 7):
        currentBoard = [row[j:j + 8] for row in _Arr_NLineInfo[i:i + 8]]
        changes1 = getMinChanges(0, 0, currentBoard, pattern1)
        changes2 = getMinChanges(0, 0, currentBoard, pattern2)
        minChanges = min(minChanges, changes1, changes2)

print(minChanges)
    