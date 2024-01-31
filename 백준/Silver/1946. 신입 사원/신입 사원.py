from ast import main
import sys
I_F_S = sys.stdin.readline

_T = int(I_F_S().rstrip())

def print_matrix(mtrx):
    for row in mtrx:
        print(row)
# 매트릭스 출력

def caseHR(t):
    _N = int(I_F_S().rstrip())
    people = [[0]*2 for _ in range(_N)]
    
    for i in range(_N):
        people[i][0], people[i][1] = map(int, I_F_S().rstrip().split())

    people.sort(key=lambda x: x[0])
    # 현재 row index (서류등수) 를 기준으로 정렬했음
    
    # print_matrix(people)
    # 예시용
    
    min_interview_rank = people[0][1]
    # 서류등수 1등의 면접점수를 기록해, 이보다 등수가 높은 사람은 서류와 면접 둘다의 항목에서
    # 둘다 등수가 서류등수 1등의 사람보다 떨어지기에(높기에), (동률X) 탈락임 
    
    count = 1
    # 서류등수 1등은 무조건 합격 (면접점수는 떨어질지라도, 서류등수에서 그 누구보다 높은 등수이기에)
    # 합격이 가능하다 (greedy 최적해 쌉가능)
    
    for i in range(_N):
        if min_interview_rank > people[i][1]:
            # 면접등수가 1등의 면접등수보다 낮으면:
            # (면.등이 높으면 서류등수와 면접등수 둘다 높기에(=면접 "점수" 가 '낮' 기에 ) 탈락)
            count += 1
            # 현재 확인중인 지원자는 합격!
            min_interview_rank = people[i][1]
            # 면접등수의 최소제한치가 올라간다. (현재 합격자는 서류등수 1등의 합격자 보다 면접등수가 낮아서 뽑힌 것이고,
            # 이는 그 다음 지원자의 면접등수는 이보다 낮아야 뽑힘. 다음 확인에서, 2등의 합격자보다 면접등수가 높으면,
            # 서류 3등 지원자는 서류 2등 합격자보다, 서류에서도 면접에서도 높은 등수를 보유한 셈으로, 뽑을수 없다.

    return count

for i in range(1, _T+1):
    print(caseHR(i))
