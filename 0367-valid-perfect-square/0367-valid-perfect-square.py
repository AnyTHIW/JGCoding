class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        
        for i in range(num//2+1):
            if (i*i < num):
                pass
            
            elif (i*i == num):
                return True
            
            elif (i*i > num):
                break
            
        return False