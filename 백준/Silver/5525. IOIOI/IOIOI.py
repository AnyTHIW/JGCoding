import sys

input = sys.stdin.readline

N_ = int(input().rstrip())
M_ = int(input().rstrip())
S_ = input().rstrip()

def countPString():
  pattString = "IOI"
  pattCnt = 0
  cnt = 0
  curr = 0

  while 0 <= curr <= M_-3:
    if S_[curr:curr+3] == pattString:
      pattCnt += 1

      if pattCnt >= N_:
        cnt += 1

      curr += 2
      
    else:
      pattCnt = 0
      curr += 1

  return cnt

print(countPString())
