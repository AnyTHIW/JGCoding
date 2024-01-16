_input = int(input())

def moveHanoiTower(sourcePosition: int, subPosition: int, targetPosition: int, diskNumber: int):
    
    # 원판이 2개이상
    if diskNumber > 1:
        moveHanoiTower(sourcePosition, targetPosition, subPosition, diskNumber-1)
        
        moveHanoiTower(sourcePosition, subPosition, targetPosition, 1)
        
        moveHanoiTower(subPosition, sourcePosition, targetPosition, diskNumber-1)
        
    #원판이 1개
    elif diskNumber > 0:
        print(sourcePosition, targetPosition)

pole_st = 1
pole_sb = 2
pole_target = 3

moveCount = (2**_input - 1)
print(moveCount)
if (_input <= 20):
    moveHanoiTower(pole_st, pole_sb, pole_target, _input)