from collections import deque as DEQUE

def solution(begin, target, words):
    
    def can_convert(word1, word2):
        diff_count = 0
        
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                diff_count += 1
                if diff_count > 1:
                    return False
                
        return diff_count == 1

    Q = DEQUE([(begin, 0)])
    vis = set()

    while Q:
        curr, steps = Q.popleft()
        if curr == target:
            return steps
        for next in words:
            if can_convert(curr, next) and next not in vis:
                vis.add(next)
                Q.append((next, steps + 1))

    return 0