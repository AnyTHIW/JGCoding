# 좌표는 다음을 기준
# (0,2) | (1,2) (2,2)
# (0,1) | (1,1) (2,1)
#        ---------
#        (1,0) (2,0)

def cut_into_four_pieces(square_size, index_X, index_Y):
    global _blue_paper, _white_paper
    
    first_data = _inputElements[index_Y][index_X]
    # 소 케이스 정복

    # 분할
    if square_size != 1:
        for i in range(index_Y, index_Y+square_size):
            for j in range(index_X, index_X+square_size):
                if _inputElements[i][j] != first_data:
                
                # 정사각형이 같은 색으로 채워지지 않았다면 분할
                    cut_into_four_pieces(square_size // 2, index_X, index_Y, )
                    cut_into_four_pieces(square_size // 2, index_X + square_size // 2, index_Y)
                    cut_into_four_pieces(square_size // 2, index_X, index_Y + square_size // 2)
                    cut_into_four_pieces(square_size // 2, index_X + square_size // 2, index_Y + square_size // 2)
                
                    return
    
    # 정복
    if first_data == 1:
        _blue_paper += 1
    else:
        _white_paper += 1
    
import sys
_squareNumber = int(input())
_inputElements = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(_squareNumber)]

_blue_paper = 0
_white_paper = 0

cut_into_four_pieces(_squareNumber, 0, 0)

print(_white_paper)
print(_blue_paper)