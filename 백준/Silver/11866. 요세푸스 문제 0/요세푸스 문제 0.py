import sys
_n = list(map(int, input().split()))

josep = [0] * _n[0]
for i in range(_n[0]):
    josep[i] = i+1

oStr = '<'
while josep:
    i = 0
    
    while _n[1] - (i+1):
        p = josep.pop(0)
        josep.append(p)
        i+=1
        
    k = josep.pop(0)
    oStr += str(k)+', '

res = oStr[:len(oStr)-2] + '>'

print(res)