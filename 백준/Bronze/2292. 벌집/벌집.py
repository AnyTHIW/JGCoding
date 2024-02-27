import sys
IFS = sys.stdin.readline

""" 주어진 number의 방을 1번 방에서부터 거쳐가는데, 이때 지나치는 방들의 최소갯수 """
def find_thresh(number: int) -> int:
    sequenceN = [1]
    
    if number == 1:
        return len(sequenceN)
    else:
        number_k = 1
        while (sequenceN[-1]<=1000000000):
            sequenceN += [sequenceN[-1]+ 6*number_k]
            if (number <= sequenceN[-1]):
                break
            number_k += 1
        length_seq = len(sequenceN)
    
    # print(f"수열 : {sequenceN}, 카운트 : {length_seq}")
    
    return length_seq
    
_N = int(IFS().rstrip())

print(find_thresh(_N))